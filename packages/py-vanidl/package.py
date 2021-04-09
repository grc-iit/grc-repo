# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyVanidl(PythonPackage):
    """This is a backport of the standard library typing module to Python
    versions older than 3.6."""

    homepage = "https://github.com/hariharan-devarajan/vanidl/wiki"
    git      = "git@github.com:hariharan-devarajan/vanidl.git"

    import_modules = ['typing']

    version('master', branch='master')
    version('0.0.1', branch='v0.0.1')

    depends_on('python@3:', type=('build', 'run'))
    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-pip', type=('build', 'run'))
    depends_on('py-numpy@1.19.0', type=('build', 'run'))
    depends_on('py-pandas@1.0.5', type=('build', 'run'))
    depends_on('py-h5py@2.10.0', type=('build', 'run'))
    depends_on('py-tensorflow@2.2.0', type=('build', 'run'))
    depends_on('py-tensorboard@2.2.2', type=('build', 'run'))
    depends_on('py-tensorboard-plugin-profile@2.10.0', type=('build', 'run'))
    depends_on('py-tensorboard-plugin-wit@1.7.0', type=('build', 'run'))
    depends_on('py-tensorflow-estimator@2.2.0',type=('build', 'run'))
