"""
Testing the installation and use of HDF5 with Clusterpy -Helper functions-
"""

from unittest import TestCase
from math import pi
from clusterpy.core.toolboxes.cluster.componentsAlg import AreaManager
from mpi4py import MPI
import h5py
import os

class TestParallelInstall(TestCase):
    def setUp(self):
        comm = MPI.COMM_WORLD
        rank = comm.Get_rank()
        self.h5file = "parallel_test.hdf5"
        self.f = h5py.File(self.h5file, 'w', driver='mpio', comm=comm)

    def tearDown(self):
        self.f.close()
        os.remove(self.h5file)

    def test_simple_group_creation(self):
        distances = self.f.create_group('distances')
