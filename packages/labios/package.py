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
#     spack install labios
#
# You can edit this file again by typing:
#
#     spack edit labios
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Labios(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "labios"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions here.
    version('main', git="https://github.com/lukemartinlogan/labios.git", branch='master')

    # FIXME: Add dependencies if required.
    depends_on('memcached')
    depends_on('libmemcached +labios')
    depends_on('nats-c')
    depends_on('nats-server')
    depends_on('mpi')
    depends_on('protobuf-c')
    depends_on('cereal')
    depends_on('cityhash')
    depends_on('yaml-cpp')
