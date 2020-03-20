
def double_lats(da):
    da.lat.data = da.lat.data * 2
    return da


# for standard name, long name etc. - need the variable id to update
# e.g. ds[f'{var_id}'].attrs['long_name'] = 'silly'
# would this need to be passed in ?
def change_lat_name(da):
    da_update_lat_name = da.rename({'lat': 'silly_lat'})
    return da_update_lat_name