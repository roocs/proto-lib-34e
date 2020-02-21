from .utils import map_args
import xarray as xr


def general_subset(dset, time=None, space=None, level=None, output_type="netcdf",
                   output_dir=None, chunk_rules=None,
                   filenamer="simple_namer"):
    """
    Example:
        dset: Xarray Dataset
        time: ("1999-01-01T00:00:00", "2100-12-30T00:00:00")
        space: (-5.,49.,10.,65)
        level: (1000.,)
        output_type: "netcdf"
        output_dir: "/cache/wps/procs/req0111"
        chunk_rules: "time:decade"
        filenamer: "facet_namer"

    :param dset:
    :param time:
    :param space:
    :param level:
    :param output_type:
    :param output_dir:
    :param chunk_rules:
    :param filenamer:
    :return:
    """
    # Convert all inputs to Xarray Datasets
    if isinstance(dset, str):
        dset = xr.open_dataset(dset)

    args = map_args(dset, time=time, space=space, level=level)

    print(f'[INFO] Calling Xarray selector with: {args}')
    result = dset.sel(**args)

#time=slice(time[0], time[1]), latitude=slice(space[1], space[3]),
#                      longitude=slice(space[0], space[2]), level=slice(level[0], level[1]),
#                      output_type=output_type, chunk_rules=chunk_rules, filenamer=filenamer)

### What about output_dir, what gets returned???
    result.to_netcdf('output1.nc') 
    return result
