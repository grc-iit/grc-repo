# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyJarvisUtil(PythonPackage):
    """This is a backport of the standard library typing module to Python
    versions older than 3.6."""

    homepage = "grc.iit.edu/docs/jarvis/jarvis-util/index"
    git      = "https://github.com/grc-iit/jarvis-util.git"

    version('main', branch='main', git='https://github.com/grc-iit/jarvis-util.git', preferred=True)
    version('priv', branch='main', git='https://github.com/lukemartinlogan/jarvis-util.git')

    depends_on('python@3:', type=('build', 'run'))
    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-pip', type=('build', 'run'))
    depends_on('py-pyyaml', type=('build', 'run'))
    depends_on('py-tabulate', type=('build', 'run'))
    
