import pytest

import daops

from .common import CMIP5_ARCHIVE_BASE


CMIP5_IDS = [
    'cmip5.output1.INM.inmcm4.rcp45.mon.ocean.Omon.r1i1p1.latest.zostoga',
    'cmip5.output1.MOHC.HadGEM2-ES.rcp85.mon.atmos.Amon.r1i1p1.latest.tas'
]


def test_subset_zostoga_with_fix():
    result = daops.subset(CMIP5_IDS[0],
                          time=('2085-01-01', '2120-12-30'),
                          data_root_dir=CMIP5_ARCHIVE_BASE,
                          output_dir='outputs')
    assert result.file_paths == ['outputs/output.nc']

def test_subset_t():
    result = daops.subset(CMIP5_IDS[1],
                          time=('2085-01-01', '2120-12-30'),
                          data_root_dir=CMIP5_ARCHIVE_BASE,
                          output_dir='outputs')
    assert result.file_paths == ['outputs/output.nc']

@pytest.mark.skip('FAILS with TypeError. Needs fixing!')
def test_subset_t_y_x():
    result = daops.subset(CMIP5_IDS[1],
                          time=('2085-01-01', '2120-12-30'),
                          space=('-20', '-10', '5', '15'),
                          data_root_dir=CMIP5_ARCHIVE_BASE,
                          output_dir='outputs')

@pytest.mark.skip('FAILS - needs fixing by bringing range into calendar range')
def test_subset_t_with_invalid_date():
    result = daops.subset(CMIP5_IDS[1],
                          time=('2085-01-01', '2120-12-31'),
                          data_root_dir=CMIP5_ARCHIVE_BASE,
                          output_dir='outputs')
