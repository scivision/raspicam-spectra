#!/usr/bin/env python
import xarray
import pandas
from pathlib import Path
from argparse import ArgumentParser


def csv2nc(csvfn: Path, ncfn: Path=None) -> xarray.DataArray:

    df = pandas.read_csv(csvfn, index_col=0, comment='#').clip(
        lower=0., upper=100.) / 100.

    darr = df.to_xarray().to_array(name='QE')

    if ncfn:
        ncfn = Path(ncfn).expanduser()
        darr.to_netcdf(ncfn)

    return darr


def main():
    p = ArgumentParser()
    p.add_argument('csvfn')
    p.add_argument('ncfn', help='NetCDF4 file to write')
    p = p.parse_args()

    csv2nc(p.csvfn, p.ncfn)


if __name__ == '__main__':
    main()
