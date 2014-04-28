from distutils.core import setup
import sys

try:
  import numpy
  import scipy

  import h5py
  import mpi4py
except ImportError:
  sys.exit("install requires: 'numpy', 'scipy', 'h5py', 'mpi4py'" +
    "optional packages: 'matplotlib', 'Polygon2'")

install_requires = ['numpy', 'scipy', 'matplotlib', 'Polygon2']
test_requires = ['nose']

setup(name = 'clusterpy',
  version = '0.10.0+exp',
  description = 'Library of spatially constrained clustering algorithms',
  long_description = """
  clusterpy is a Python library with algorithms for spatially constrained
  clustering. clusterpy offers you some of the most cited algorithms for
  spatial aggregation.""",
  author = 'RiSE Group',
  author_email = 'software@rise-group.org',
  url = 'http://www.rise-group.org/section/Software/clusterPy/',

  test_suite = 'nose.collector',
  include_package_data = True,
  packages = [
    'clusterpy.core',
    'clusterpy.core.contiguity',
    'clusterpy.core.data',
    'clusterpy.core.geometry',
    'clusterpy.core.toolboxes',
    'clusterpy.core.toolboxes.cluster',
    'clusterpy.core.toolboxes.rimaps',
    'clusterpy.core.toolboxes.sstats',
    'clusterpy.core.toolboxes.cluster.componentsAlg',
    'clusterpy.core.toolboxes.sstats.basic',
    'clusterpy.core.toolboxes.sstats.inequality'
    ]
  )
