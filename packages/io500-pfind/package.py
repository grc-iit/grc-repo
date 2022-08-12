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
#     spack install io500-pfind
#
# You can edit this file again by typing:
#
#     spack edit io500-pfind
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os

class Io500Pfind(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/mchaarawi/pfind"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    version('master.isc22', git='https://github.com/VI4IO/pfind.git', commit='62c3a7e31')
    version('daos.isc22', git='https://github.com/mchaarawi/pfind', branch='mfu_integration')

    variant('daos', default=False, description='Compile io500 for DAOS')
    conflicts('+daos', when='@master.isc22', msg="Cannot build master with daos")
    conflicts('~daos', when='@daos.isc22', msg="Must specify building pfind with daos")

    patch('cmakelists_isc22.patch', when='~daos @master.isc22')
    patch('cmakelists_daos_isc22.patch', when='+daos @daos.isc22')

    # FIXME: Add dependencies if required.
    depends_on('lz4')
    depends_on('mpi')
    depends_on('io500-mpifileutils', when='~daos @master.isc22')
    depends_on('io500-mpifileutils@daos.isc22 +daos', when='+daos @daos.isc22')

    def setup_run_environment(self, env):
        env.prepend_path('CPATH', os.path.join(self.prefix, 'include'))
        env.prepend_path('INCLUDE', os.path.join(self.prefix, 'include'))
        env.prepend_path('LIBRARY_PATH', os.path.join(self.prefix, 'lib'))
        env.prepend_path('LIBRARY_PATH', os.path.join(self.prefix, 'lib64'))
        env.prepend_path('LD_LIBRARY_PATH', os.path.join(self.prefix, 'lib64'))
        env.prepend_path('LD_LIBRARY_PATH', os.path.join(self.prefix, 'lib64'))
        env.prepend_path('PATH', os.path.join(self.prefix, 'bin'))