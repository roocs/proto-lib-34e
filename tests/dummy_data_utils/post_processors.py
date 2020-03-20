
def drop_lat(ds, *args, **kwargs):
    ds_drop_lat = ds.drop_dims(*args, **kwargs)
    return ds_drop_lat


def update_attrs(ds, *args, **kwargs):
    var_id = kwargs["var_id"]
    for key, value in kwargs.items():
        if key is not "var_id":
            ds[f'{var_id}'].attrs[f'{key}'] = f'{value}'
    return ds


def change_data(ds, *args, **kwargs):
    var_id = kwargs["var_id"]
    ds[f'{var_id}'].data = ds[f'{var_id}'].data + args[0]
    return ds


