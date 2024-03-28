# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.boost import Boost


class Thrift(AutotoolsPackage):
    """Software framework for scalable cross-language services development.

    Thrift combines a software stack with a code generation engine to
    build services that work efficiently and seamlessly between C++,
    Java, Python, PHP, Ruby, Erlang, Perl, Haskell, C#, Cocoa,
    JavaScript, Node.js, Smalltalk, OCaml and Delphi and other languages.

    """

    homepage = "https://thrift.apache.org"
    git = "https://github.com/apache/thrift.git"
    list_depth = 1

    maintainers("thomas-bouvier")

    version("0.20.0", branch="v0.20.0")

    variant("pic", default=True, description="Build position independent code")
    variant("c", default=True, description="Build support for C-family languages")
    variant("java", default=False, description="Build support for java")
    variant("python", default=True, description="Build support for python")

    depends_on("pkgconfig", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("boost@1.53:")

    # TODO: replace this with an explicit list of components of Boost,
    # for instance depends_on('boost +filesystem')
    # See https://github.com/spack/spack/pull/22303 for reference
    depends_on(Boost.with_default_variants)
    depends_on("bison", type="build")
    depends_on("flex", type="build")
    depends_on("openssl")

    # Variant dependencies
    depends_on("zlib-api", when="+c")
    depends_on("libevent", when="+c")

    depends_on("java@7:", when="+java")
    depends_on("ant", when="+java")

    extends("python", when="+python")
    depends_on("py-setuptools", type=("build", "run"), when="+python")
    depends_on("py-six@1.7.2:", type=("build", "run"), when="@0.10.0:+python")
    depends_on("py-tornado", type=("build", "run"), when="+python")
    depends_on("py-twisted", type=("build", "run"), when="+python")
    depends_on("py-zope-interface", type=("build", "run"), when="+python")
    depends_on("py-pure-sasl", type=("build", "run"), when="+python")
    depends_on("scons", type=("build", "run"), when="+python")

    patch(
        "https://github.com/apache/thrift/pull/2511.patch?full_index=1",
        sha256="8523c97eccb31b084241b4061db830c4ef940042b37ba8ddfdcdd23d92325b89",
        when="@0.16.0",
    )

    def configure_args(self, spec):
        options = []
        options.append("--with-boost=%s" % spec["boost"].prefix)
        options.append("--enable-tests=no")

        options.append("--with-nodejs=no")
        options.append("--with-c=%s" % ("yes" if "+c" in spec else "no"))
        options.append("--with-python=%s" % ("yes" if "+python" in spec else "no"))
        options.append("--with-java=%s" % ("yes" if "+java" in spec else "no"))
        options.append("--with-go=no")
        options.append("--with-lua=no")
        options.append("--with-php=no")
        options.append("--with-kotlin=no")
        options.append("--with-ruby=no")
        options.append("--with-qt4=no")
        return options

    def setup_build_environment(self, env):
        if "+pic" in self.spec:
            env.append_flags("CFLAGS", self.compiler.cc_pic_flag)
            env.append_flags("CXXFLAGS", self.compiler.cxx_pic_flag)

    # def install(self, spec, prefix):
    #     env["PY_PREFIX"] = prefix
    #
    #     # configure options
    #     options = ["--prefix=%s" % prefix]
    #
    #     options.append("--with-boost=%s" % spec["boost"].prefix)
    #     options.append("--enable-tests=no")
    #
    #     options.append("--with-nodejs=no")
    #     options.append("--with-c=%s" % ("yes" if "+c" in spec else "no"))
    #     options.append("--with-python=%s" % ("yes" if "+python" in spec else "no"))
    #     options.append("--with-java=%s" % ("yes" if "+java" in spec else "no"))
    #     options.append("--with-go=no")
    #     options.append("--with-lua=no")
    #     options.append("--with-php=no")
    #     options.append("--with-kotlin=no")
    #     options.append("--with-ruby=no")
    #     options.append("--with-qt4=no")
    #
    #     configure(*options)
    #
    #     make()
    #     make("install")
