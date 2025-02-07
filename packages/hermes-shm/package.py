from spack import *

class HermesShm(CMakePackage):
    homepage = "https://github.com/lukemartinlogan/hermes-shm/wiki"
    git = "https://github.com/grc-iit/hermes-shm.git"
    url = "https://github.com/grc-iit/hermes-shm/archive/refs/tags/v1.2.0.tar.gz"

    # Branch versions
    version('main', branch='master')
    version('dev', branch='dev')
    version('priv', branch='dev', git='https://github.com/lukemartinlogan/hermes-shm.git')
    
    # Versions used by IoWarp CTE
    version('2.0.0', tag='v2.0.0', git='https://github.com/grc-iit/hermes-shm.git')

    # Versions used by Hermes 1.x
    version("1.2.0", tag="v1.2.0", git='https://github.com/grc-iit/hermes-shm.git')

    # Main variants
    variant('debug', default=False, description='Build shared libraries')
    variant('mochi', default=True, description='Build with mochi-thallium support')
    variant('cereal', default=True, description='Build with cereal support')
    variant('boost', default=True, description='Build with boost support')
    variant('mpiio', default=True, description='Build with MPI support')
    variant('vfd', default=False, description='Build with HDF5 support')
    variant('zmq', default=False, description='Build ZeroMQ tests')
    variant('adios', default=False, description='Build Adios support')
    variant('elf', default=False, description='Build elf toolkit')
    variant('python', default=False, description='Build python')
    variant('jarvis', default=True, description='Install jarvis deployment tool')
    variant('nocompile', default=False, description='Do not compile the library (used for dev purposes)')

    # Required deps
    depends_on('catch2@3.0.1')
    depends_on('yaml-cpp')
    depends_on('doxygen')

    # Machine variants
    variant('ares', default=False, description='Build in ares')
    depends_on('libfabric fabrics=sockets,tcp,udp,verbs,mlx,rxm,rxd,shm',
               when='+ares')

    # Main dependencies
    depends_on('libelf', when='+elf')
    depends_on('mochi-thallium+cereal@0.10.1', when='+mochi')
    depends_on('argobots@1.1+affinity', when='+mochi')
    depends_on('cereal', when='+cereal')
    depends_on('boost@1.7: +context +fiber +coroutine +regex +system +filesystem +serialization +pic +math',
               when='+boost')
    depends_on('mpi', when='+mpiio')
    depends_on('hdf5@1.14.0', when='+vfd')
    depends_on('libzmq', when='+zmq')
    depends_on('adios2', when='+adios')

    # Python dependencies
    depends_on('py-jarvis-cd', when='+jarvis')
    depends_on('py-pybind11', when='+python')
    depends_on('python', when='+python')
    depends_on('py-pip', when='+python')
    # depends_on('py-scipy', when='+python')
    # depends_on('py-numpy', when='+python')
    # depends_on('py-scikit-learn', when='+python')
    # depends_on('py-pandas', when='+python')

    # Compress variant
    variant('compress', default=False,
            description='Build with compression support')
    depends_on('lzo', when='+compress')
    depends_on('bzip2', when='+compress')
    depends_on('zstd', when='+compress')
    depends_on('lz4', when='+compress')
    depends_on('zlib', when='+compress')
    depends_on('xz', when='+compress')
    depends_on('brotli', when='+compress')
    depends_on('snappy', when='+compress')
    depends_on('c-blosc2', when='+compress')

    # Encryption variant
    variant('encrypt', default=False,
            description='Build with encryption support')
    depends_on('openssl', when='+encrypt')

    def cmake_args(self):
        args = []
        # args.append(self.define('BUILD_HSHM_TESTS', 'OFF'))
        if '+debug' in self.spec:
            args.append(self.define('CMAKE_BUILD_TYPE', 'Debug'))
        if '+vfd' in self.spec:
            args.append(self.define('HSHM_ENABLE_VFD', 'ON'))
        if '+compress' in self.spec:
            args.append(self.define('HSHM_ENABLE_COMPRESS', 'ON'))
        if '+encrypt' in self.spec:
            args.append(self.define('HSHM_ENABLE_ENCRYPT', 'ON'))
        if '+mochi' in self.spec:
            args.append(self.define('HSHM_RPC_THALLIUM', 'ON'))
        if '+zmq' in self.spec:
            args.append(self.define('HSHM_ENABLE_ZMQ_TESTS', 'ON'))
        if '+elf' in self.spec:
            args.append(self.define('HSHM_USE_ELF', 'ON'))
        if '+nocompile' in self.spec:
            args.append(self.define('HSHM_NO_COMPILE', 'ON'))
        return args