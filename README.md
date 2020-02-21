# proto-lib-34e

Prototype for 34e libraries and interfaces

## Installation

Use Python 3.7

And install dependencies:

```
pip install -r requirements.txt
```

Set some useful environment variables:

```
export PYTHONPATH=.
export PYTHONWARNINGS=ignore
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

```
pytest -v test
```

### Test datasets

Datasets used for testing are:

```
1. cmip5.output1.MOHC.HadGEM2-ES.rcp85.mon.atmos.Amon.r1i1p1.latest.tas
 @CEDA: /badc/cmip5/data/cmip5/output1/MOHC/HadGEM2-ES/rcp85/mon/atmos/Amon/r1i1p1/latest/tas/*.nc
```



