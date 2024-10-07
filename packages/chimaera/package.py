from spack import *

class Chimaera(CMakePackage):
    homepage = "http://www.cs.iit.edu/~scs/assets/projects/Hermes/Hermes.html"
    git = "https://github.com/lukemartinlogan/chimaera.git"

    version('master',
            branch='main', submodules=True)

    depends_on('hermes_shm@master')

    # Common across hermes_shm and hermes
    variant('debug', default=False, description='Build shared libraries')
    variant('ares', default=False, description='Enable full libfabric install')
    variant('zmq', default=False, description='Build ZeroMQ tests')
    variant('python', default=True, description='Support python libs for ML')

    depends_on('hermes_shm+compress')
    depends_on('hermes_shm+encrypt')
    depends_on('hermes_shm+elf')
    depends_on('hermes_shm+mochi')
    depends_on('hermes_shm+debug', when='+debug')
    depends_on('hermes_shm+mpiio')
    depends_on('hermes_shm+cereal')
    depends_on('hermes_shm+boost')
    depends_on('hermes_shm+ares', when='+ares')
    depends_on('hermes_shm+zmq', when='+zmq')
    depends_on('py-pybind11', when='+python')

    def cmake_args(self):
        args = []
        if '+debug' in self.spec:
            args.append('-DCMAKE_BUILD_TYPE=Debug')
        else:
            args.append('-DCMAKE_BUILD_TYPE=Release')
        return args

    def set_include(self, env, path):
        env.append_flags('CFLAGS', '-I{}'.format(path))
        env.append_flags('CXXFLAGS', '-I{}'.format(path))
        env.prepend_path('INCLUDE', '{}'.format(path))
        env.prepend_path('CPATH', '{}'.format(path))

    def set_lib(self, env, path):
        env.prepend_path('LIBRARY_PATH', path)
        env.prepend_path('LD_LIBRARY_PATH', path)
        env.append_flags('LDFLAGS', '-L{}'.format(path))
        env.prepend_path('PYTHONPATH', '{}'.format(path))

    def set_flags(self, env):
        self.set_include(env, '{}/include'.format(self.prefix))
        self.set_include(env, '{}/include'.format(self.prefix))
        self.set_lib(env, '{}/lib'.format(self.prefix))
        self.set_lib(env, '{}/lib64'.format(self.prefix))
        env.prepend_path('CMAKE_PREFIX_PATH', '{}/cmake'.format(self.prefix))
        env.prepend_path('CMAKE_MODULE_PATH', '{}/cmake'.format(self.prefix))

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        self.set_flags(spack_env)

    def setup_run_environment(self, env):
        self.set_flags(env)
