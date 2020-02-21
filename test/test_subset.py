import pytest

import wps_lib


CMIP5_ID1 = 'cmip5.output1.MOHC.HadGEM2-ES.rcp85.mon.atmos.Amon.r1i1p1.latest.tas'


def test_subset_t():
    resp = wps_lib.subset_wps_process(CMIP5_ID1, time='2085-01-01/2120-12-30')
    assert(isinstance(resp, wps_lib.WPSResponse))
    assert(resp.urls[0] == 'http://download?path=outputs/requests/0/output.nc')


def test_subset_t_y_x():
    resp = wps_lib.subset_wps_process(CMIP5_ID1, time='2085-01-01/2120-12-30', 
                                      space='-20,-10,5,15')
    assert(isinstance(resp, wps_lib.WPSResponse))
    assert(resp.urls[0] == 'http://download?path=outputs/requests/1/output.nc')


@pytest.mark.skip('FAILS - needs fixing by bringing range into calendar range')
def test_subset_t_with_invalid_date():
    resp = wps_lib.subset_wps_process(CMIP5_ID1, time='2085-01-01/2120-12-31')
    assert(isinstance(resp, wps_lib.WPSResponse))

