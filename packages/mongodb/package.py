from spack import *
class Mongodb(SConsPackage):
  """FIXME: Put a proper description of your package here."""

  # FIXME: Add a proper url for your package's homepage here.
  homepage = "https://github.com/mongodb/mongo"
  url      = "https://github.com/mongodb/mongo/archive/r4.0.6.tar.gz"

  version('4.1.10',     sha256='b6e0cd151f95728276a02a9b0d86a1582b1b30d5763fd6b5c0e1a0c488e7bc67')
  version('4.0.9',      sha256='746a29345dca7538440d676412c9e0e6ae1507fa19fa59113616edfa85e501b5')
  version('4.0.8',      sha256='22446721638cfe7e0520138b80c19d2005ded7c950c4da7fd86aa1f00a0bd108')
  version('4.0.7',      sha256='cb42d440bc4a4d1b6f1fb35d36dd8c9ac6474b89ca3b47497c9eccff5e66abb5')
  version('4.0.6',      sha256='5db85f06b2a0b2ae393339a4aed1366928aaef2b46c7c32826fa87c3217dc6f7')
  version('3.6.12',     sha256='5d6e99edbea4395c5de18fead0db882cac87ee3c8eb4ad446d91c33ab91cd175')

  variant('languages',
    default='c,c++,fortran',
    values=('ada', 'brig', 'c', 'c++', 'fortran',
            'go', 'java', 'jit', 'lto', 'objc', 'obj-c++'),
    multi=True,
    description='Compilers and runtime libraries to build')

  # FIXME: Add dependencies if required.

  depends_on('gmp@6.1.0', when='@4.0.6:')
  depends_on('isl@0.16.1', when='@4.0.6:')
  depends_on('mpc@1.0.3', when='@4.0.6:')
  depends_on('mpfr@3.1.4', when='@4.0.6:')
  depends_on('gcc@9.3.0', when='@4.0.6:')
  depends_on('curl@7.68.0', when='@4.0.6:')
  depends_on('py-pyyaml', when='@4.0.6:', type=('build', 'run'))
  depends_on('py-typing', when='@4.0.6:', type=('build', 'run'))
  depends_on('py-psutil', when='@4.0.6:', type=('build', 'run'))

  depends_on('python@3.8.3', when='@4.0.6')

  def build_args(self, spec, prefix):
    # FIXME: Add arguments to pass to build.
    # FIXME: If not needed delete this functiona
    args = [
            'MONGO_VERSION={}'.format(self.version),
            '--disable-warnings-as-errors'
            ]
    return args

  def install_args(self, spec, prefix):
    args = [
            'MONGO_VERSION={}'.format(self.version),
            '--disable-warnings-as-errors'
           ]
    return args
