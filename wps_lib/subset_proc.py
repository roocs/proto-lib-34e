import daops
import daops.config as dconfig

from .wps_helpers import WPSResponse, WPSRequest, translate_args


def subset_wps_process(data_refs, time=None, space=None, level=None, pre_checked=False):
    """
    Example:
        data_refs: "cmip6.ukesm1.r1.gn.tasmax.v20200101"
        time: ("1999-01-01T00:00:00", "2100-12-30T00:00:00")
        space: (-5.,49.,10.,65)
        level: (1000.,)
        pre_checked: False

    :param data_refs:
    :param time:
    :param space:
    :param level:
    :param pre_checked:
    :return:
    """

    request = WPSRequest(**vars())

    if pre_checked and not daops.is_characterised(data_refs, require_all=True):
        return WPSResponse('Data has not been pre-checked')

    config_args = {'output_dir': request.directory,
                   'chunk_rules': dconfig.chunk_rules,
                   'filenamer': dconfig.filenamer}

    kwargs = translate_args(**{'time': time, 'space': space, 'level': level})
    kwargs.update(config_args)

    result = daops.subset(data_refs, **kwargs)
    return WPSResponse(result=result)
