from spack import *

class Hermes(CMakePackage):
    homepage = "https://grc.iit.edu/docs/hermes/main-scenario"
    url = "https://github.com/HDFGroup/hermes/tarball/master"
    git = "https://github.com/HDFGroup/hermes.git"

    version('master',
            branch='master', 
            submodules=True,
            git='https://github.com/HDFGroup/hermes.git')
    version('dev', branch='dev',
             submodules=True, 
             git='https://github.com/HDFGroup/hermes.git')
    
    # Versions for Hermes 1.x
    version('1.2.1', tag='v1.2.1', git='https://github.com/HDFGroup/hermes.git', submodules=True)

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

    depends_on('hermes-shm@1.2.0')
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

    def setup_run_environment(self, env):
        # This is for the interceptors
        env.prepend_path('LD_LIBRARY_PATH', self.prefix.lib)
