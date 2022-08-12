# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install io500-ior
#
# You can edit this file again by typing:
#
#     spack edit io500-ior
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os, shutil

class DaosIor(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/hpc/ior.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    version('2.1', git='https://github.com/hpc/ior.git', commit='d3574d536643475269d37211e283b49ebd6732d7')

    phases = ['bootstrap', 'configure', 'build', 'install', 'install_headers']

    variant('daos', default='none', description='Compile io500 for DAOS', multi=False,
            values=('none', 'isc22'))

    # FIXME: Add dependencies if required.
    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')

    depends_on('io500-mpifileutils', when='daos=none')
    depends_on('io500-mpifileutils daos=isc22', when='daos=isc22')

    def setup_run_environment(self, env):
        env.prepend_path('CPATH', os.path.join(self.prefix, 'include'))
        env.prepend_path('INCLUDE', os.path.join(self.prefix, 'include'))
        env.prepend_path('LIBRARY_PATH', os.path.join(self.prefix, 'lib'))
        env.prepend_path('LIBRARY_PATH', os.path.join(self.prefix, 'lib64'))
        env.prepend_path('LD_LIBRARY_PATH', os.path.join(self.prefix, 'lib64'))
        env.prepend_path('LD_LIBRARY_PATH', os.path.join(self.prefix, 'lib64'))
        env.prepend_path('PATH', os.path.join(self.prefix, 'bin'))

    def configure_args(self):
        args = []
        if self.spec.variants['daos'].value != 'none':
            args.append('--with-daos={}'.format(self.spec['daos'].prefix))
        return args

    def bootstrap(self, spec, prefix):
        bstrap = Executable('./bootstrap')
        bstrap()

    def install_headers(self, spec, prefix):
        os.mkdir(self.spec.prefix.include)
        for f in os.listdir('src'):
            if '.h' in f:
                shutil.copy(os.path.join('src', f), self.spec.prefix.include)
