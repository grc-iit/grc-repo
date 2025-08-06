from spack.package import *

class Dtio(CMakePackage):
    homepage = "https://github.com/grc-iit/DTIO"
    git = "git@github.com:grc-iit/DTIO.git"

    version('main', branch='main', submodules=True, preferred=True)

    variant('mpi', default=True, description='Enable MPI support')
    variant('liburing', default=False, description='Enable liburing support')
    variant('nocompile', default=False, description='Do not compile the library (used for dev purposes)')
    variant('iowarp', default=True, description='Enable iowarp runtime')

    depends_on('iowarp-runtime', when='+iowarp')
    depends_on('hdf5')
    depends_on('liburing', when='+liburing')
    depends_on('mpi', when='+mpi')

    def cmake_args(self):
        args = []
        if '+mpi' in self.spec:
            args.append(self.define('DTIO_ENABLE_MPI', 'ON'))
        else:
            args.append(self.define('DTIO_ENABLE_MPI', 'OFF'))
        if '+liburing' in self.spec:
            args.append(self.define('DTIO_ENABLE_LIBURING', 'ON'))
        else:
            args.append(self.define('DTIO_ENABLE_LIBURING', 'OFF'))
        if '+nocompile' in self.spec:
            args.append(self.define('DTIO_NO_COMPILE', 'ON'))
        else:
            args.append(self.define('DTIO_NO_COMPILE', 'OFF'))
        return args 
