from collections import OrderedDict


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
    resp = OrderedDict()

    for dref in data_refs:
        _is_char = is_dataref_characterised(dref)

        if require_all and not _is_char:
            return False

        resp[dref] = is_dataref_characterised(dref)

    return resp


def consolidate(data_refs):
    return data_refs


def normalise(data_refs):
    return [xr.open_mfdataset(data_ref) for data_ref in data_refs]


class ResultSet(object):

    def __init__(self):
        self._results = OrderedDict()

    def add(self, data_ref, result):
        self._results[data_ref] = result

