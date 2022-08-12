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

class DaosIo500(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/IO500/io500.git"
    #phases = ['configure', 'build', 'install']

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2.0', git="https://github.com/IO500/io500.git", branch="io500-isc21")

    variant('daos', default='none', description='Compile io500 for DAOS', multi=False,
            values=('none', 'isc22'))
    patch('cmakelists_daos.patch')

    # FIXME: Add dependencies if required.
    depends_on('daos@2.1', when="daos=isc22")
    depends_on('io500-mpifileutils', when="daos=none")
    depends_on('io500-mpifileutils daos=isc22', when="daos=isc22")
    depends_on('io500-ior', when="daos=none")
    depends_on('io500-ior daos=isc22', when="daos=isc22")