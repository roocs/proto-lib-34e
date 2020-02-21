import collections
import glob

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


def _consolidate_data_ref(dref):
    if dref[0] == '/':
        return dref

    if dref.find('cmip5') > -1:
        dref = '/badc/cmip5/data/' + dref.replace('.', '/') + '/*.nc'

    return dref
 

def consolidate(data_refs, **kwargs):
    data_refs = _wrap_sequence(data_refs)
    filtered_refs = collections.OrderedDict()

    for dref in data_refs:

        consolidated = _consolidate_data_ref(dref)

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


def normalise(data_refs):
    print(f'[INFO] Working on data refs: {data_refs}')
    norm_dsets = collections.OrderedDict()

    for data_ref, file_paths in data_refs.items():
        xr_dset = xr.open_mfdataset(file_paths)
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


