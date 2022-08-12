# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
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
#     spack install io500-mpifileutils
#
# You can edit this file again by typing:
#
#     spack edit io500-mpifileutils
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os

class DaosMpifileutils(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/mchaarawi/mpifileutils"
    phases = ['build', 'install']

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    version('2.0', git="https://github.com/mchaarawi/mpifileutils", branch="pfind_integration")

    variant('daos', default='none', description='Compile io500 for DAOS', multi=False,
            values=('none', 'isc22'))

    # FIXME: Add dependencies if required.
    depends_on('dtcmp')
    depends_on('io500-libcircle', when='daos=none')
    depends_on('io500-libcircle daos=isc22', when='daos=isc22')

    depends_on('libarchive')
    depends_on('lwgrp')
    depends_on('mpi')

    def setup_run_environment(self, env):
        env.prepend_path('CPATH', os.path.join(self.prefix, 'include'))
        env.prepend_path('INCLUDE', os.path.join(self.prefix, 'include'))
        env.prepend_path('LIBRARY_PATH', os.path.join(self.prefix, 'lib'))
        env.prepend_path('LIBRARY_PATH', os.path.join(self.prefix, 'lib64'))
        env.prepend_path('LD_LIBRARY_PATH', os.path.join(self.prefix, 'lib64'))
        env.prepend_path('LD_LIBRARY_PATH', os.path.join(self.prefix, 'lib64'))
        env.prepend_path('PATH', os.path.join(self.prefix, 'bin'))

    def cmake_args(self, spec, prefix):
        args = [
            '-DCMAKE_INSTALL_PREFIX={}'.format(prefix),
            '-DENABLE_XATTRS=OFF',
            '-DWITH_DTCMP_PREFIX={}'.format(spec['dtcmp'].prefix),
            '-DWITH_LibCircle_PREFIX={}'.format(spec['io500-libcircle'].prefix)
        ]
        return args

    def build(self, spec, prefix):
        cmake(*self.cmake_args(spec, prefix))
        make()

    def install(self, spec, prefix):
        make('install')