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
#     spack install io500-libcircle
#
# You can edit this file again by typing:
#
#     spack edit io500-libcircle
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Io500Libcircle(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/hpc/libcircle/releases/download/v0.3/libcircle-0.3.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.3.0', sha256='5ce38eb5b3c2b394bca1316310758f276c893dd3f4c15d7bc14ea05d3110ce58')

    variant('optimize', default=True, description='Compile libcircle with some optimizations')
    patch('optimize.patch', when='+optimize')

    # FIXME: Add dependencies if required.
    depends_on('mpi')
