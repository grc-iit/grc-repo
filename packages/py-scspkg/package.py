# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScspkg(PythonPackage):
    """This is a backport of the standard library typing module to Python
    versions older than 3.6."""

    homepage = "https://github.com/grc-iit/scspkg"
    git      = "https://github.com/grc-iit/scspkg.git"

    version('main', branch='master', preferred=True)

    depends_on('python@3:', type=('build', 'run'))
    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-pip', type=('build', 'run'))
    depends_on('py-jarvis-util', type=('build', 'run'))
    
