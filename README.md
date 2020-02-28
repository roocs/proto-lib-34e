# proto-lib-34e

Prototype for 34e libraries and interfaces

## Installation

Use Python 3.7.

And run the installation:

```
pip install .
```

Or in development mode:

```
pip install -e .
pip install -r requirements_dev.txt
```

### Use a conda environment

You can use a conda environment with Python 3.7.

```
conda env create -f environment.yml
conda activate daops
```

Run the installation:

```
pip install -e .
```

### JASMIN-specific installation

One-off install:

```
module load jaspy
python -m venv venv --system-site-packages

source venv/bin/activate
pip install -r requirements.txt
```

Each time you log in again:

```
module load jaspy
source venv/bin/activate

export PYTHONPATH=.
export PYTHONWARNINGS=ignore
```

## Testing

Configure the data root:
```
export CMIP5_ARCHIVE_BASE=/badc/cmip5/data/
```

And run the tests:
```
pytest -v tests

OR (if it fails):

python -m pytest -v tests
```

### Test datasets

Datasets used for testing are:

```
1. cmip5.output1.MOHC.HadGEM2-ES.rcp85.mon.atmos.Amon.r1i1p1.latest.tas
 @CEDA: /badc/cmip5/data/cmip5/output1/MOHC/HadGEM2-ES/rcp85/mon/atmos/Amon/r1i1p1/latest/tas/*.nc

2. cmip5.output1.INM.inmcm4.rcp45.mon.ocean.Omon.r1i1p1.latest.zostoga
 @CEDA: /badc/cmip5/data/cmip5/output1/INM/inmcm4/rcp45/mon/ocean/Omon/r1i1p1/latest/zostoga
```
