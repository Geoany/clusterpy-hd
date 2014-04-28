#!/bin/bash
HDF5FILE="hdf5-1.8.12"
wget --quiet http://www.hdfgroup.org/ftp/HDF5/current/src/$HDF5FILE.tar.gz
tar xzf $HDF5FILE.tar.gz
cd $HDF5FILE
HDF5DIR=`pwd`
CC=mpicc ./configure --enable-parallel --enable-shared
make
#make check
make install
cd ..
H5PYFILE="h5py-2.3.0"
wget --quiet https://pypi.python.org/packages/source/h/h5py/$H5PYFILE.tar.gz
tar xzf $H5PYFILE.tar.gz
cd $H5PYFILE
CC=mpicc python setup.py build --mpi --hdf5=$HDF5DIR/hdf5/
python setup.py install
