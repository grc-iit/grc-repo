from spack import *

class MegaMmap(CMakePackage):
    homepage = "http://www.cs.iit.edu/~scs/assets/projects/Hermes/Hermes.html"
    git = "https://github.com/grc-iit/mega_mmap.git"

    version('main',
            branch='master', submodules=True)
    version('priv', branch='dev',
            git='https://github.com/lukemartinlogan/mega_mmap.git', submodules=True)
    depends_on('hermes@master')
    depends_on('arrow +parquet')

    def cmake_args(self):
        args = []
        return args
