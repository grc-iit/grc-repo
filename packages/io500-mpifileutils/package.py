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

class Io500Mpifileutils(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/mchaarawi/mpifileutils"
    phases = ['build', 'install']

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    version('0.11.1', url='https://github.com/hpc/mpifileutils/archive/v0.10.tar.gz', sha256='e2cba53309b5b3ee581b6ff82e4e66f54628370cce694c34224ed947fece32d4')
    version('0.11', url='https://github.com/hpc/mpifileutils/archive/v0.10.tar.gz', sha256='f5dc1b39077b3c04f79b2c335c4fd80306f8c57ecfbcacbb82cf532caf02b5fd')
    version('0.10.1', url='https://github.com/hpc/mpifileutils/archive/v0.10.tar.gz', sha256='4c8409ef4140f6f557d0e93f0c1267baf5d893c203b29fb7a33d9bc3c5a5d25c')
    version('0.10', url='https://github.com/hpc/mpifileutils/archive/v0.10.tar.gz', sha256='5a71a9acd9841c3c258fc0eaea942f18abcb40098714cc90462b57696c07e3c5')

    version('daos.isc22', git="https://github.com/mchaarawi/mpifileutils", branch="pfind_integration")

    #Variants
    variant('daos', default=False, description='Compile io500 for DAOS')
    conflicts('+daos', when='@0.10:0.11.1')
    conflicts('~daos', when='@daos.isc22')

    # FIXME: Add dependencies if required.
    depends_on('dtcmp')
    depends_on('io500-libcircle')
    depends_on('libcap')
    depends_on('attr')
    depends_on('libarchive')
    depends_on('lwgrp')
    depends_on('mpi')
    depends_on('daos@2.1', when='+daos @daos.isc22')

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