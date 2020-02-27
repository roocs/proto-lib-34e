import collections
import glob
import os
import importlib
import json

import xarray as xr


def _wrap_sequence(obj):
    if isinstance(obj, str):
        obj = [obj]
    return obj


def is_dataref_characterised(data_ref):
    return True


def is_characterised(data_refs, require_all=False):
    """
    Takes in an individual data reference or a sequence of them.
    Returns an ordered dictionary of data_refs with a boolean value
    for each stating whether the dataset has been characterised.

    If `require_all` is True: return a single Boolean value.

    :param data_refs: one or more data references
    :param require_all: Boolean to require that all must be characterised
    :return: Ordered Dictionary OR Boolean (if `require_all` is True)
    """
    data_refs = _wrap_sequence(data_refs)
    resp = collections.OrderedDict()

    for dref in data_refs:
        _is_char = is_dataref_characterised(dref)

        if require_all and not _is_char:
            return False

        resp[dref] = is_dataref_characterised(dref)

    return resp


def _consolidate_data_ref(dref, data_root_dir=None):
    if dref[0] == '/':
        return dref

    if dref.find('cmip5') > -1 and data_root_dir is not None:
        dref = data_root_dir.rstrip('/') + '/' + dref.replace('.', '/') + '/*.nc'

    return dref


def consolidate(data_refs, data_root_dir, **kwargs):
    data_refs = _wrap_sequence(data_refs)
    filtered_refs = collections.OrderedDict()

    for dref in data_refs:

        consolidated = _consolidate_data_ref(dref, data_root_dir)

        if 'time' in kwargs:
            required_years = set(range(*[int(_.split('-')[0]) for _ in kwargs['time']]))

            file_paths = glob.glob(consolidated)
            print(f'[INFO] Testing {len(file_paths)} files in time range: ...')
            files_in_range = []

            for i, fpath in enumerate(file_paths):
                print(f'[INFO] File {i}: {fpath}')
                ds = xr.open_dataset(fpath)

                found_years = set([int(_) for _ in ds.time.dt.year])

                if required_years.intersection(found_years):
                    files_in_range.append(fpath)

            print(f'[INFO] Kept {len(files_in_range)} files')
            consolidated = files_in_range[:]

        filtered_refs[dref] = consolidated

    return filtered_refs


def resolve_import(import_path):
    """
    Deconstructs path, imports module and returns callable.

    :param import path: module and function as 'x.y.func' (of any depth)
    :return: callable.
    """
    # Split last item off path
    parts = import_path.split('.')
    ipath = '.'.join(parts[:-1])
    func_name = parts[-1]

    # Import module then send the args and kwargs to the function
    try:
        module = importlib.import_module(ipath)
        func = getattr(module, func_name)
    except Exception as exc:
        raise ImportError(f'Could not import function from path: {import_path}')

    return func


class Fixer(object):

    FIX_DIR = './fixes'

    def __init__(self, ds_id):
        self.ds_id = ds_id
        self._lookup_fix()

    def _lookup_fix(self):
        fix_file = os.path.join(self.FIX_DIR, f'{self.ds_id}.json')

        if not os.path.isfile(fix_file):
            self.pre_processor = None
            self.post_processor = None

        else:
            content = json.load(open(fix_file))
            pre_processor = content.get('pre_processor', None)
            post_processor = content.get('post_processor', None)

            if pre_processor:
                self.pre_processor = resolve_import(pre_processor['func'])
            else:
                self.pre_processor = None

            if post_processor:
                self.post_processor = (resolve_import(post_processor['func']),
                                       post_processor.get('args', None) or [],
                                       post_processor.get('kwargs', None) or {})


def open_dataset(ds_id, file_paths):
    # Wrap xarray open with required args

    fixer = Fixer(ds_id)
    if fixer.pre_processor:
        print(f'[INFO] Loading data with pre_processor: {fixer.pre_processor.__name__}')
    else:
        print(f'[INFO] Loading data')

    ds = xr.open_mfdataset(file_paths, preprocess=fixer.pre_processor,
                           use_cftime=True, combine='by_coords')

    if fixer.post_processor:
        func, args, kwargs = fixer.post_processor
        print(f'[INFO] Running post-processing function: {func.__name__}')
        ds = func(ds, *args, **kwargs)

    return ds


def normalise(data_refs):
    print(f'[INFO] Working on data refs: {data_refs}')
    norm_dsets = collections.OrderedDict()

    for data_ref, file_paths in data_refs.items():

        xr_dset = open_dataset(data_ref, file_paths)
        norm_dsets[data_ref] = xr_dset

    return norm_dsets


class ResultSet(object):


    def __init__(self, inputs=None):
        self._results = collections.OrderedDict()
        self.metadata = {'inputs': inputs, 'process': 'something', 'version': 0.1}
        self.file_paths = []

    def add(self, data_ref, result):
        self._results[data_ref] = result
        self.file_paths.append(result)
