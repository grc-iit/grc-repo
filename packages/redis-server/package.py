# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RedisServer(MakefilePackage):
    """Hiredis is a minimalistic C client library for the Redis database."""

    homepage = "https://github.com/redis/hiredis"
    url      = "https://github.com/redis/redis/archive/6.0.6.tar.gz"

    version('6.0.6',sha256='e7cedb37077be2e4ba6323bb3c6c8da027701b9093ebb2f8d15a0c67e145b7c0')

    def install(self, spec, prefix):
        make('PREFIX={0}'.format(prefix), 'install')

    def set_include(self, env, path):
        env.append_flags('CFLAGS', '-I{}'.format(path))
        env.append_flags('CXXFLAGS', '-I{}'.format(path))

    def set_lib(self, env, path):
        env.prepend_path('LD_LIBRARY_PATH', path)
        env.append_flags('LDFLAGS', '-L{}'.format(path))

    def set_flags(self, env):
        self.set_include(env, '{}/include'.format(self.prefix))
        self.set_include(env, '{}/include'.format(self.prefix))
        self.set_lib(env, '{}/lib'.format(self.prefix))
        self.set_lib(env, '{}/lib64'.format(self.prefix))

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        self.set_flags(spack_env)

    def setup_run_environment(self, env):
        self.set_flags(env)
