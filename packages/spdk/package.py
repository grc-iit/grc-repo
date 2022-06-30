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
import os

#pip3 install defusedxml distro junit_xml pyxattr tabulate scons pyyaml pyelftools

class Spdk(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    git      = "https://github.com/spdk/spdk"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['lukemartinlogan']

    # FIXME: Add proper versions and checksums here.
    version('22.05', git="https://github.com/spdk/spdk", branch='v22.05.x', submodules=True)
    phases = ["prepare", "configure", "build", "install"]

    depends_on('scons')
    depends_on('dpdk')

    def setup_run_environment(self, env):
        env.prepend_path('CPATH', os.path.join(self.prefix, 'include'))
        env.prepend_path('INCLUDE', os.path.join(self.prefix, 'include'))
        env.prepend_path('LIBRARY_PATH', os.path.join(self.prefix, 'lib'))
        env.prepend_path('LIBRARY_PATH', os.path.join(self.prefix, 'lib64'))
        env.prepend_path('LD_LIBRARY_PATH', os.path.join(self.prefix, 'lib64'))
        env.prepend_path('LD_LIBRARY_PATH', os.path.join(self.prefix, 'lib64'))
        env.prepend_path('PATH', os.path.join(self.prefix, 'bin'))

    def prepare(self, spec, prefix):
        deps = Executable('sudo')
        deps('bash', './scripts/pkgdep.sh')