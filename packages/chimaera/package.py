from spack.package import *

class Chimaera(CMakePackage):
    homepage = "http://www.cs.iit.edu/~scs/assets/projects/Hermes/Hermes.html"
    git = "https://github.com/iowarp/iowarp-runtime.git"

    version('main',
            branch='main', submodules=True, preferred=True)
    version('dev',
            branch='dev', submodules=True)
    version('priv',
            branch='main', submodules=True, git='https://github.com/lukemartinlogan/chimaera.git')

    # Common across hermes-shm and hermes
    variant('debug', default=False, description='Build shared libraries')
    variant('ares', default=False, description='Enable full libfabric install')
    variant('zmq', default=False, description='Build ZeroMQ tests')
    variant('jarvis', default=True, description='Install jarvis deployment tool')
    variant('nocompile', default=False, description='Do not compile the library (used for dev purposes)')
    variant('depsonly', default=False, description='Only install dependencies')

    depends_on('hermes-shm@main', when='@main')
    depends_on('hermes-shm@dev', when='@dev')
    depends_on('hermes-shm@priv', when='@priv')
    
    depends_on('hermes-shm+compress')
    depends_on('hermes-shm+encrypt')
    depends_on('hermes-shm+elf')
    depends_on('hermes-shm+mochi')
    depends_on('hermes-shm+debug', when='+debug')
    depends_on('hermes-shm+mpiio')
    depends_on('hermes-shm+cereal')
    depends_on('hermes-shm+boost')
    depends_on('hermes-shm+ares', when='+ares')
    depends_on('hermes-shm+zmq', when='+zmq')
    depends_on('hermes-shm+python')
    depends_on('hermes-shm -nocompile', when='~nocompile')
    depends_on('hermes-shm +nocompile', when='+nocompile')
    depends_on('py-jarvis-cd', when='+jarvis')
    depends_on('py-chimaera-util')
    depends_on('mpi')

    def cmake_args(self):
        args = []
        if '+debug' in self.spec:
            args.append('-DCMAKE_BUILD_TYPE=Debug')
        else:
            args.append('-DCMAKE_BUILD_TYPE=Release')
        if '+nocompile' in self.spec or '+depsonly' in self.spec:
            args.append('-DCHIMAERA_NO_COMPILE=ON')
        return args
