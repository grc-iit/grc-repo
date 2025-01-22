from spack import *

class ChiNettest(CMakePackage):
    homepage = "https://github.com/lukemartinlogan/chi-nettest.git"
    git = "https://github.com/lukemartinlogan/chi-nettest.git"
    version('main', branch='main')
    
    # Required deps
    depends_on('hermes-shm@dev +mochi -nocompile')

    def cmake_args(self):
        args = []
        return args