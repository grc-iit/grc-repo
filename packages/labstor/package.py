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
#     spack install labstor
#
# You can edit this file again by typing:
#
#     spack edit labstor
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Labstor(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/lukemartinlogan/labstor.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    version('master', git='https://github.com/lukemartinlogan/labstor.git')

    variant('uring', default=True, description='Compile LabStor with IOUring')
    variant('spdk', default=True, description='Compile LabStor with SPDK')
    variant('dpdk', default=False, description='Compile LabStor with DPDK')
    variant('bench', default=True, description='Compile LabStor with benchmark tests')

    # FIXME: Add dependencies if required.
    depends_on('mpi')
    depends_on('yaml-cpp')
    depends_on('spdk', when='+spdk')
    depends_on('dpdk', when='+dpdk')
    depends_on('filebench', when='+bench')
    depends_on('ycsb', when='+bench')
    depends_on('fxmark', when='+bench')
    depends_on('fio', when='+bench')

    def cmake_args(self):
        args = [
            f"-DWITH_SPDK={self.spec['SPDK']}",
            f"-DWITH_DPDK={self.spec['DPDK']}"
        ]
        return args
