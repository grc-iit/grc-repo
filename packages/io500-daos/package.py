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
#     spack install io500-daos
#
# You can edit this file again by typing:
#
#     spack edit io500-daos
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import shutil

class Io500Daos(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/IO500/io500.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.21', git="https://github.com/IO500/io500.git", branch="io500-isc21")
    phases = ['install']

    patch('io500_Makefile.patch')
    patch('io500_prepare.patch')

    # FIXME: Add dependencies if required.
    depends_on('libarchive')
    depends_on('libcircle')
    depends_on('lwgrp')
    depends_on('dtcmp')
    depends_on('daos')
    depends_on('mpifileutils-daos')

    def install(self, spec, prefix):
        prepare = Executable('./prepare.sh')
        prepare()
        shutil.copytree(os.getcwd(), prefix)

    def build_environment(self, spec, prefix):
        pass

