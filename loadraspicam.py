#!/usr/bin/env python
"""
Loads specified spectrum of Raspberry Pi camera
digitized by Koen Hufkens

Michael Hirsch
"""
from pathlib import Path
import xarray
from matplotlib.pyplot import figure, show
from matplotlib.ticker import MultipleLocator
try:
    import seaborn as sns
    sns.set_context('talk')
except ImportError:
    pass


def loadT(fn: Path) -> xarray.DataArray:
    fn = Path(fn).expanduser()

    dat = xarray.open_dataarray(fn)

    return dat


def plotT(T: xarray.DataArray, name: str = ''):

    fg = figure()
    ax = fg.gca()
    ax.set_title(f'{name} Optical Transmission')

    wl = T.wavelength_nm

    ax.plot(wl, T.loc['red_qe', :], color='r')
    ax.plot(wl, T.loc['green_qe', :], color='g')
    ax.plot(wl, T.loc['blue_qe', :], color='b')
    ax.invert_xaxis()

    ax.set_ylabel('Transmission')
    ax.grid(True, which='both')
    ax.xaxis.set_minor_locator(MultipleLocator(25))

    ax.yaxis.set_minor_locator(MultipleLocator(.05))

    ax.set_xlabel('wavelength [nm]')


def main():
    plotT(loadT('OV5647.nc'), 'Omnivision OV5647 (PiCam v1)')

    plotT(loadT('IMX219.nc'), 'Sony IMX219 (PiCam v2)')

    show()


if __name__ == '__main__':
    main()
