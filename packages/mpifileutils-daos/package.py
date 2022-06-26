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
#     spack install mpifileutils-daos
#
# You can edit this file again by typing:
#
#     spack edit mpifileutils-daos
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *

class MpifileutilsDaos(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/mchaarawi/mpifileutils"
    phases = ['build', 'install']

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    version('1.0.0', git="https://github.com/mchaarawi/mpifileutils", branch="pfind_integration")

    patch('cmakelists.patch')

    # FIXME: Add dependencies if required.
    depends_on('dtcmp')
    depends_on('libcircle')
    depends_on('libarchive')
    depends_on('lwgrp')
    depends_on('daos')
    depends_on('mpi')

    def cmake_args(self, spec, prefix):
        dtcmp = spack.spec.Spec(spec['dtcmp']).concretized().format('{prefix}')
        libcircle = spack.spec.Spec(spec['dtcmp']).concretized().format('{prefix}')
        args = [
            '-DCMAKE_INSTALL_PREFIX={}'.format(prefix),
            '-DENABLE_XATTRS=OFF',
            '-DWITH_DTCMP_PREFIX={}'.format(dtcmp),
            '-DWITH_LibCircle_PREFIX={}'.format(libcircle)
        ]
        return args

    def build(self, spec, prefix):
        cmake(*self.cmake_args(spec, prefix))
        make()

    def install(self, spec, prefix):
        make('install')