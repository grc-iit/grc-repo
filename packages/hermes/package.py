from spack import *

class Hermes(CMakePackage):
    homepage = "http://www.cs.iit.edu/~scs/assets/projects/Hermes/Hermes.html"
    url = "https://github.com/HDFGroup/hermes/tarball/master"
    git = "https://github.com/HDFGroup/hermes.git"

    version('master',
            branch='master', submodules=True)
    version('dev', branch='dev', submodules=True)
    version('priv', branch='dev',
            git='https://github.com/lukemartinlogan/hermes.git', submodules=True)
    version("1.0.5-beta", sha256="1f3ba51a8beda4bc1314d6541b800de1525f5e233a6f498fcde6dc43562ddcb7")
    version("1.0.0-beta", sha256="301084cced32aa00532ab4bebd638c31b0512c881ffab20bf5da4b7739defac2")

    depends_on('hermes_shm')

    # Common across hermes_shm and hermes
    variant('mpiio', default=True, description='Enable MPI I/O adapter')
    variant('stdio', default=True, description='Enable STDIO adapter')
    variant('debug', default=False, description='Build shared libraries')
    variant('vfd', default=False, description='Enable HDF5 VFD')
    variant('ares', default=False, description='Enable full libfabric install')
    variant('zmq', default=False, description='Build ZeroMQ tests')
    variant('adios', default=False, description='Build Adios tests')
    variant('encrypt', default=False, description='Build Adios tests')
    variant('compress', default=False, description='Build Adios tests')

    depends_on('hermes_shm+elf')
    depends_on('hermes_shm+mochi')
    depends_on('hermes_shm+debug', when='+debug')
    depends_on('hermes_shm+mpiio')
    depends_on('hermes_shm+cereal')
    depends_on('hermes_shm+boost')
    depends_on('hermes_shm+ares', when='+ares')
    depends_on('hermes_shm+zmq', when='+zmq')
    depends_on('hermes_shm+vfd', when='+vfd')
    depends_on('hermes_shm+adios', when='+adios')
    depends_on('hermes_shm+encrypt', when='+encrypt')
    depends_on('hermes_shm+compress', when='+compress')
    depends_on('libelf')
    depends_on('chimaera')

    def cmake_args(self):
        args = []
        if '+debug' in self.spec:
            args.append('-DCMAKE_BUILD_TYPE=Debug')
        else:
            args.append('-DCMAKE_BUILD_TYPE=Release')
        if '+mpiio' in self.spec:
            args.append('-DHERMES_ENABLE_MPIIO_ADAPTER=ON')
            if 'openmpi' in self.spec:
                args.append('-DHERMES_OPENMPI=ON')
            elif 'mpich' in self.spec:
                args.append('-DHERMES_MPICH=ON')
        if '+stdio' in self.spec:
            args.append('-HERMES_ENABLE_STDIO_ADAPTER=ON')
        if '+vfd' in self.spec:
            args.append('-HERMES_ENABLE_VFD=ON')
        if '+compress' in self.spec:
            args.append(self.define('HERMES_ENABLE_COMPRESS', 'ON'))
        if '+encrypt' in self.spec:
            args.append(self.define('HERMES_ENABLE_ENCRYPT', 'ON'))
        return args
