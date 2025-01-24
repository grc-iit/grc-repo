from spack import *

class Iowarp(CMakePackage):
    homepage = "https://grc.iit.edu/docs/hermes/main-scenario"
    url = "https://github.com/HDFGroup/hermes/tarball/master"
    git = "https://github.com/iowarp/content-transfer-engine.git"

    version('master',
            branch='master', 
            git='https://github.com/iowarp/content-transfer-engine.git')
    version('dev', branch='dev',
             git='https://github.com/iowarp/content-transfer-engine.git')
    version('priv', branch='dev',
            git='https://github.com/lukemartinlogan/hermes.git')
    
    # Common across hermes-shm and hermes
    variant('mpiio', default=True, description='Enable MPI I/O adapter')
    variant('stdio', default=True, description='Enable STDIO adapter')
    variant('debug', default=False, description='Build shared libraries')
    variant('vfd', default=False, description='Enable HDF5 VFD')
    variant('ares', default=False, description='Enable full libfabric install')
    variant('adios', default=False, description='Build Adios tests')
    variant('encrypt', default=False, description='Include encryption libraries')
    variant('compress', default=False, description='Include compression libraries')
    variant('jarvis', default=True, description='Install jarvis deployment tool')
    variant('nocompile', default=False, description='Do not compile the library (used for dev purposes)')

    depends_on('chimaera')
    depends_on('chimaera -nocompile', when='~nocompile')
    depends_on('chimaera +nocompile', when='+nocompile')

    depends_on('hermes-shm@2:')
    depends_on('hermes-shm+elf')
    depends_on('hermes-shm+debug', when='+debug')
    depends_on('hermes-shm+mpiio')
    depends_on('hermes-shm+ares', when='+ares')
    depends_on('hermes-shm+vfd', when='+vfd')
    depends_on('hermes-shm+adios', when='+adios')
    depends_on('hermes-shm+encrypt', when='+encrypt')
    depends_on('hermes-shm+compress', when='+compress')
    depends_on('py-jarvis-cd@master', when='+jarvis')

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
        if '+nocompile' in self.spec:
            args.append(self.define('HERMES_NO_COMPILE', 'ON'))
        return args
