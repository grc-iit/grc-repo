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
#     spack install orangefs
#
# You can edit this file again by typing:
#
#     spack edit orangefs
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import os
from spack.package import *


class Orangefs(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "http://download.orangefs.org/current/source/orangefs-2.9.8.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2.9.8', sha256='589f7b6c4c8ea9b96b61427f9005ad0be258cb43702b47d9f304c8128ca25e30')

    depends_on('bison')
    depends_on('berkeley-db')
    #kernel-header, kernel-devel

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = [
            "--enable-shared",
            "--enable-fuse"
        ]
        #Kernel < 5.0 requires --with-kernel
        if int(os.uname().release.split('.')[0]) < 5:
            args.append(f"--with-kernel=/lib/modules/{os.uname().release}/build")
        return args
