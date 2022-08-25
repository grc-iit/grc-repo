# Copyright 2012-2020 Lawrence Livermore National Security, LLC and other
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
#     spack install io500
#
# You can edit this file again by typing:
#
#     spack edit io500
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import shutil
import os

class Io500Cmake(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/IO500/io500.git"
    #phases = ['configure', 'build', 'install']

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('isc22', git="https://github.com/IO500/io500.git", branch="io500-isc22")

    variant('daos', default=False, description='Compile io500 for DAOS')

    patch('cmakelists_isc22.patch', when='~daos @isc22')
    patch('cmakelists_daos_isc22.patch', when='+daos @isc22')

    # FIXME: Add dependencies if required.
    depends_on('io500-ior@master.isc22', when="~daos @isc22")
    depends_on('io500-pfind@master.isc22', when="~daos @isc22")

    depends_on('daos@2.1', when="+daos @isc22")
    depends_on('io500-mpifileutils@daos.isc22 +daos', when="+daos @isc22")
    depends_on('io500-ior@daos.isc22 +daos', when="+daos @isc22")
    depends_on('io500-pfind@daos.isc22 +daos', when="+daos @isc22")