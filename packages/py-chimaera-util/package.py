# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyChimaeraUtil(PythonPackage):
    homepage = "grc.iit.edu/docs/jarvis/jarvis-cd/index"
    git      = "https://github.com/grc-iit/chimaera-util.git"

    import_modules = ['typing']

    version('master', branch='master', git='https://github.com/grc-iit/chimaera-util.git', preferred=True)
    version('priv', branch='master', git='https://github.com/lukemartinlogan/chimaera-util.git')

    depends_on('python@3:', type=('build', 'run'))
    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-pip', type=('build', 'run'))
    depends_on('py-pyyaml', type=('build', 'run'))
    depends_on('py-jarvis-util', type=('build', 'run'))
    depends_on('py-jarvis-util@priv', type=('build', 'run'), when='@priv')

