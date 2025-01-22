# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyJarvisCd(PythonPackage):
    homepage = "https://github.com/lukemartinlogan/jarvis-cd.git"
    git      = "https://github.com/lukemartinlogan/jarvis-cd.git"

    import_modules = ['typing']

    version('master', branch='master')

    depends_on('python@3:', type=('build', 'run'))
    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-pip', type=('build', 'run'))
    depends_on('py-pandas', type=('build', 'run'))
    depends_on('py-pyyaml', type=('build', 'run'))
    depends_on('py-jarvis-util', type=('build', 'run'))
    depends_on('chi_nettest', type=('build', 'run'))

