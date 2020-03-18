import pytest

from daops import api, utils

from .common import CMIP5_ARCHIVE_BASE

import numpy as np

CMIP5_IDS = [
    'cmip5.output1.INM.inmcm4.rcp45.mon.ocean.Omon.r1i1p1.latest.zostoga',
    'cmip5.output1.MOHC.HadGEM2-ES.rcp85.mon.atmos.Amon.r1i1p1.latest.tas',
    'cmip5.output1.MOHC.HadGEM2-ES.historical.mon.land.Lmon.r1i1p1.latest.rh'
]


# setup for tests - including making fix functions
def setup_module(module):
    module.CMIP5_ARCHIVE_BASE = 'mini-esgf-data/test_data/badc/cmip5/data'
    utils.Fixer.FIX_DIR = 'tests/test_fixes'


# could test rounding coordinates but haven't worked out how to get full dataarray back yet.
def pre_process(da):
    return da


def post_process(ds, *args, **kwargs):
    ds_lat_renamed = ds.drop_dims(*args, **kwargs)
    return ds_lat_renamed


def test_subset_with_pre_and_post_process_fix():
    result = api.subset(CMIP5_IDS[1],
                        time=('2085-01-01', '2120-12-30'),
                        data_root_dir=CMIP5_ARCHIVE_BASE,
                        output_dir='outputs')
    assert result.file_paths == ['outputs/output.nc']


def test_subset_with_pre_process_fix():
    result = api.subset(CMIP5_IDS[2],
                        time=('1975-01-01', '2002-12-30'),
                        data_root_dir=CMIP5_ARCHIVE_BASE,
                        output_dir='outputs')
    assert result.file_paths == ['outputs/output.nc']


def test_subset_with_post_fixes():
    result = api.subset(CMIP5_IDS[0],
                        time=('2085-01-01', '2120-12-30'),
                        data_root_dir=CMIP5_ARCHIVE_BASE,
                        output_dir='outputs')
    assert result.file_paths == ['outputs/output.nc']


def teardown_module(module):
    module.CMIP5_ARCHIVE_BASE = 'mini-esgf-data/test_data/badc/cmip5/data'
    utils.Fixer.FIX_DIR = 'tests/test_fixes'

