# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "base"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

$requirements = <<END
sudo apt-get update -qq
sudo apt-get install -y build-essential libopenmpi-dev
sudo apt-get install -y git-core
sudo apt-get install -y python-dev python-numpy
sudo apt-get install -y python-scipy
sudo apt-get install -y python-nose python-pip python-matplotlib
sudo apt-get install -y python-mpi4py cython
END
  config.vm.provision :shell, :inline => $requirements

  pipinstall = "/usr/bin/pip install Polygon2"
  #config.vm.provision :shell, :inline => pipinstall

$HDF5_requirements = <<END
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
END

  config.vm.provision :shell, :inline => $HDF5_requirements
end
