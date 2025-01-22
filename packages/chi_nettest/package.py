from spack import *

class ChiNettest(CMakePackage):
    homepage = "https://github.com/lukemartinlogan/hermes-shm/wiki"
    git = "https://github.com/lukemartinlogan/chi-nettest.git"
    version('master', branch='master')
    version('dev', branch='dev')
    
    # Required deps
    depends_on('hermes_shm@dev+mochi')

    def cmake_args(self):
        args = []
        return args