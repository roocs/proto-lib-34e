import re
import pytest

import wps_lib


CMIP5_IDS = [
    'cmip5.output1.INM.inmcm4.rcp45.mon.ocean.Omon.r1i1p1.latest.zostoga',
    'cmip5.output1.MOHC.HadGEM2-ES.rcp85.mon.atmos.Amon.r1i1p1.latest.tas'
]


def _matches_path(p):
    return re.match('http://download\?path=outputs/requests/[0-9]+/output\.nc', p)


def test_subset_zostoga_with_fix():
    resp =  wps_lib.subset_wps_process(CMIP5_IDS[0], time='2085-01-01/2120-12-30')
    assert(isinstance(resp, wps_lib.WPSResponse))
    assert(_matches_path(resp.urls[0]))


def test_subset_t():
    resp = wps_lib.subset_wps_process(CMIP5_IDS[1], time='2085-01-01/2120-12-30')
    assert(isinstance(resp, wps_lib.WPSResponse))
    assert(_matches_path(resp.urls[0]))


def test_subset_t_y_x():
    resp = wps_lib.subset_wps_process(CMIP5_IDS[1], time='2085-01-01/2120-12-30', 
                                      space='-20,-10,5,15')
    assert(isinstance(resp, wps_lib.WPSResponse))
    assert(_matches_path(resp.urls[0]))


@pytest.mark.skip('FAILS - needs fixing by bringing range into calendar range')
def test_subset_t_with_invalid_date():
    resp = wps_lib.subset_wps_process(CMIP5_IDS[1], time='2085-01-01/2120-12-31')
    assert(isinstance(resp, wps_lib.WPSResponse))

