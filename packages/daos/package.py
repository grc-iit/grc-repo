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
#     spack install daos
#
# You can edit this file again by typing:
#
#     spack edit daos
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import shutil

"""
clang \
libibverbs-dev \
libipmctl-dev \
libnuma-dev \
libopenmpi-dev \
librdmacm-dev \
locales \
openjdk-8-jdk \
"""


class Daos(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    git      = "https://github.com/daos-stack/daos.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['lukemartinlogan']

    # FIXME: Add proper versions and checksums here.
    version('2.0', git="https://github.com/daos-stack/daos.git", branch='release/2.0', submodules=True)
    phases = ["prepare", "build", "install"]

    """
    #depends_on('e2fsprogs@1.46.5')
    depends_on('gcc')
    depends_on('go')
    depends_on('git')
    depends_on('boost')
    depends_on('cmake')
    depends_on('autoconf')
    depends_on('file')
    depends_on('libfuse')
    depends_on('libaio')
    depends_on('curl')
    depends_on('kmod')
    depends_on('cmocka')
    depends_on('cunit')
    depends_on('hwloc@1.9')
    depends_on('json-c')
    depends_on('lz4')
    depends_on('mpi')
    depends_on('rdma-core')
    depends_on('openssl')
    depends_on('libtool')
    depends_on('libunwind')
    depends_on('libyaml')
    depends_on('maven')
    depends_on('meson')
    depends_on('numactl')
    depends_on('meson')
    depends_on('ninja')
    depends_on('patchelf')
    depends_on('pciutils')
    depends_on('pkg-config')
    depends_on('python')
    depends_on('py-defusedxml')
    depends_on('py-distro')
    depends_on('py-junit-xml')
    depends_on('py-pyelftools')
    depends_on('py-xattr')
    depends_on('py-tabulate')
    depends_on('scons')
    depends_on('libuuid')
    depends_on('valgrind')
    depends_on('yasm')
    """

    def prepare(self, spec, prefix):
        deps = Executable('sudo')
        if shutil.which('apt') is not None:
            deps('./utils/scripts/install-ubuntu20.sh')
        else:
            deps('./utils/scripts/install-el8.sh')
            deps('./utils/scripts/install-centos7.sh')
            deps('./utils/scripts/install-leap15.sh')

    def build_args(self, spec, prefix):
        args = [
            "PREFIX={}".format(prefix),
            '--config=force',
            '--build-deps=yes'
        ]
        return args

    def build(self, spec, prefix):
        scons = Executable('scons')
        scons(*self.build_args(spec, prefix))

    def install(self, spec, prefix):
        scons = Executable('scons')
        scons('install')

