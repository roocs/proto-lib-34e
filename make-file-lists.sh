#!/bin/bash

cd /home/users/astephen/roocs/proto-lib-34e/

for d in cmip5 cmip6 cordex; do

    find -L /badc/$d/data/ -iname "*.nc" -type l > file-list-${d}.txt

done
