#!/usr/bin/env python3
"""
Loads specified spectrum of Raspberry Pi camera
digitized by Koen Hufkens

Michael Hirsch
"""
from __future__ import division,absolute_import
from os.path import expanduser
import h5py
from pandas import DataFrame
from matplotlib.pyplot import figure,show
from matplotlib.ticker import MultipleLocator
import seaborn as sns
sns.set_context('talk')

def loadT14(h5fn):
    h5fn = expanduser(h5fn)

    with h5py.File(h5fn,'r',libver='latest') as f:
        T = DataFrame(index=f['/T/1.4um']['wavelength'],
                      columns=['red','green','blue'])
        T['red']   = f['/T/1.4um']['red']
        T['green'] = f['/T/1.4um']['green']
        T['blue'] = f['/T/1.4um']['blue']

    return T

def plotT(T,log,sensor):
    assert isinstance(T,DataFrame)

    ax = figure(figsize=(12,6)).gca()
    ax.plot(T.index,T['red'],color='r')
    ax.plot(T.index,T['green'],color='g')
    ax.plot(T.index,T['blue'],color='b')
    ax.invert_xaxis()
    ax.set_title('Raspberry Pi OV5647 Optical Transmission '+sensor)
    ax.set_xlabel('wavelength [nm]')
    ax.set_ylabel('Transmission')
    ax.grid(True,which='both')
    ax.xaxis.set_minor_locator(MultipleLocator(25))

    if log:
        ax.set_yscale('log')
    else:
        ax.yaxis.set_minor_locator(MultipleLocator(.05))


if __name__ == '__main__':
    T = loadT14('raspicamOV5647.h5')
    plotT(T,False,'$1.4\mu$m sensor')
    plotT(T,True,'$1.4\mu$m sensor')

    show()