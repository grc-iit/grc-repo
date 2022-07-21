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
#     spack install nats-server
#
# You can edit this file again by typing:
#
#     spack edit nats-server
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class NatsServer(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/nats-io/nats-server.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    version('2.8.4', git='https://github.com/nats-io/nats-server.git', branch='v2.8.4')
    version('2.8.3', git='https://github.com/nats-io/nats-server.git', branch='v2.8.3')
    version('2.8.2', git='https://github.com/nats-io/nats-server.git', branch='v2.8.2')
    version('2.8.1', git='https://github.com/nats-io/nats-server.git', branch='v2.8.2')
    version('2.8.0', git='https://github.com/nats-io/nats-server.git', branch='v2.8.2')

    # FIXME: Add dependencies if required.
    depends_on('go')

    def setup_run_environment(self, env):
        env.prepend_path('GOPATH', self.prefix)

    def install(self, spec, prefix):
        go = Executable('go')
        go('install')
