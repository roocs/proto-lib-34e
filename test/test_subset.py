import wps_lib

CMIP5_ID = 'cmip5.output1.MOHC.HadGEM2-ES.rcp85.mon.atmos.Amon.r1i1p1.latest.tas'


def test_subset_t():
    resp = wps_lib.subset_wps_process(CMIP5_ID, time='2085-01-01/2120-12-31')
    assert(isinstance(resp, wps_lib.WPSResponse))

