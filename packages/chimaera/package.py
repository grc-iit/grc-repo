from spack import *

class Chimaera(CMakePackage):
    homepage = "http://www.cs.iit.edu/~scs/assets/projects/Hermes/Hermes.html"
    git = "https://github.com/lukemartinlogan/chimaera.git"

    version('master',
            branch='main', submodules=True)

    depends_on('hermes_shm')

    # Common across hermes_shm and hermes
    variant('debug', default=False, description='Build shared libraries')
    variant('ares', default=False, description='Enable full libfabric install')
    variant('zmq', default=False, description='Build ZeroMQ tests')
    variant('python', default=True, description='Support python libs for ML')

    depends_on('hermes_shm@dev')
    depends_on('hermes_shm+elf')
    depends_on('hermes_shm+mochi')
    depends_on('hermes_shm+debug', when='+debug')
    depends_on('hermes_shm+mpiio')
    depends_on('hermes_shm+cereal')
    depends_on('hermes_shm+boost')
    depends_on('hermes_shm+ares', when='+ares')
    depends_on('hermes_shm+zmq', when='+zmq')
    depends_on('hermes_shm+python', when='+python')

    def cmake_args(self):
        args = []
        if '+debug' in self.spec:
            args.append('-DCMAKE_BUILD_TYPE=Debug')
        else:
            args.append('-DCMAKE_BUILD_TYPE=Release')
        return args
