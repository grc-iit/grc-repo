# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Arrow(CMakePackage, CudaPackage):
    """A cross-language development platform for in-memory data.

    This package contains the C++ bindings.
    """

    homepage = "https://arrow.apache.org"
    git = "https://github.com/apache/arrow.git"

    version("15.0.1", branch='apache-arrow-15.0.1')

    # depends_on("boost@1.60: +filesystem +system")
    # depends_on("cmake@3.2.0:", type="build")
    # depends_on("flatbuffers")
    # depends_on("llvm@:11 +clang", when="+gandiva @:3", type="build")
    # depends_on("llvm@:12 +clang", when="+gandiva @:4", type="build")
    # depends_on("llvm@:13 +clang", when="+gandiva @:7", type="build")
    # depends_on("llvm@:14 +clang", when="+gandiva @8:", type="build")
    # depends_on("lz4", when="+lz4")
    # depends_on("ninja", type="build")
    # depends_on("openssl", when="+gandiva @6.0.0:")
    # depends_on("openssl", when="@4.0.0:")
    # depends_on("orc", when="+orc")
    # depends_on("protobuf", when="+gandiva")
    # depends_on("py-numpy", when="+python")
    # depends_on("python", when="+python")
    # depends_on("rapidjson")
    # depends_on("re2+shared", when="+compute")
    # depends_on("re2+shared", when="+gandiva")
    # depends_on("re2+shared", when="+python")
    # depends_on("snappy~shared", when="+snappy @9:")
    # depends_on("snappy~shared", when="@8:")
    depends_on("thrift+pic", when="+parquet")
    # depends_on("utf8proc@2.7.0: +shared", when="+compute")
    # depends_on("utf8proc@2.7.0: +shared", when="+gandiva")
    # depends_on("utf8proc@2.7.0: +shared", when="+python")
    # depends_on("xsimd@8.1.0:", when="@9.0.0:")
    # depends_on("zlib-api", when="+zlib @9:")
    # depends_on("zlib-api", when="@:8")
    # conflicts("^zlib~pic")
    # depends_on("zstd", when="+zstd @9:")
    # depends_on("zstd", when="@:8")

    variant("brotli", default=False, description="Build support for Brotli compression")
    variant(
        "build_type",
        default="Release",
        description="CMake build type",
        values=("Debug", "FastDebug", "Release"),
    )
    variant(
        "compute", default=False, description="Computational kernel functions and other support"
    )
    variant("gandiva", default=False, description="Build Gandiva support")
    variant(
        "glog",
        default=False,
        description="Build libraries with glog support for pluggable logging",
    )
    variant(
        "hdfs",
        default=False,
        description="Integration with libhdfs for accessing the Hadoop Filesystem",
    )
    variant("ipc", default=True, description="Build the Arrow IPC extensions")
    variant("jemalloc", default=False, description="Build the Arrow jemalloc-based allocator")
    variant("lz4", default=False, description="Build support for lz4 compression")
    variant("orc", default=False, description="Build integration with Apache ORC")
    variant("parquet", default=False, description="Build Parquet interface")
    variant("python", default=False, description="Build Python interface")
    variant("shared", default=True, description="Build shared libs")
    variant("snappy", default=False, description="Build support for Snappy compression")
    variant("tensorflow", default=False, description="Build Arrow with TensorFlow support enabled")
    variant("zlib", default=False, description="Build support for zlib (gzip) compression")
    variant("zstd", default=False, description="Build support for ZSTD compression")

    root_cmakelists_dir = "cpp"

    def patch(self):
        """Prevent `-isystem /usr/include` from appearing, since this confuses gcc."""
        filter_file(
            r"(include_directories\()SYSTEM ", r"\1", "cpp/cmake_modules/ThirdpartyToolchain.cmake"
        )

        if self.spec.satisfies("@:2.0.0"):
            filter_file(
                r'set\(ARROW_LLVM_VERSIONS "10" "9" "8" "7"\)',
                'set(ARROW_LLVM_VERSIONS "11" "10" "9" "8" "7")',
                "cpp/CMakeLists.txt",
            )
            filter_file(
                r"#include <llvm/Support/DynamicLibrary\.h>",
                r"#include <llvm/Support/DynamicLibrary.h>"
                + "\n"
                + r"#include <llvm/Support/Host.h>",
                "cpp/src/gandiva/engine.cc",
            )

    def cmake_args(self):
        args = ["-DARROW_DEPENDENCY_SOURCE=SYSTEM", "-DARROW_NO_DEPRECATED_API=ON"]

        if self.spec.satisfies("+shared"):
            args.append(self.define("BUILD_SHARED", "ON"))
        else:
            args.append(self.define("BUILD_SHARED", "OFF"))
            args.append(self.define("BUILD_STATIC", "ON"))

        if self.spec.satisfies("@:0.11.99"):
            # ARROW_USE_SSE was removed in 0.12
            # see https://issues.apache.org/jira/browse/ARROW-3844
            args.append(self.define("ARROW_USE_SSE", "ON"))

        args.append(self.define_from_variant("ARROW_COMPUTE", "compute"))
        args.append(self.define_from_variant("ARROW_CUDA", "cuda"))
        args.append(self.define_from_variant("ARROW_GANDIVA", "gandiva"))
        args.append(self.define_from_variant("ARROW_GLOG", "glog"))
        args.append(self.define_from_variant("ARROW_HDFS", "hdfs"))
        args.append(self.define_from_variant("ARROW_IPC", "ipc"))
        args.append(self.define_from_variant("ARROW_JEMALLOC", "jemalloc"))
        args.append(self.define_from_variant("ARROW_ORC", "orc"))
        args.append(self.define_from_variant("ARROW_PARQUET", "parquet"))
        args.append(self.define_from_variant("ARROW_PYTHON", "python"))
        args.append(self.define_from_variant("ARROW_TENSORFLOW", "tensorflow"))
        args.append(self.define_from_variant("ARROW_WITH_BROTLI", "brotli"))
        args.append(self.define_from_variant("ARROW_WITH_LZ4", "lz4"))
        args.append(self.define_from_variant("ARROW_WITH_SNAPPY", "snappy"))
        args.append(self.define_from_variant("ARROW_WITH_ZLIB", "zlib"))
        args.append(self.define_from_variant("ARROW_WITH_ZSTD", "zstd"))

        if not self.spec.dependencies("re2"):
            args.append(self.define("ARROW_WITH_RE2", False))
        if not self.spec.dependencies("utf8proc"):
            args.append(self.define("ARROW_WITH_UTF8PROC", False))

        if self.spec.satisfies("@:8"):
            args.extend(
                [
                    self.define("FLATBUFFERS_HOME", self.spec["flatbuffers"].prefix),
                    self.define("RAPIDJSON_HOME", self.spec["rapidjson"].prefix),
                    self.define("ZSTD_HOME", self.spec["zstd"].prefix),
                    self.define("ZLIB_HOME", self.spec["zlib-api"].prefix),
                    self.define("ZLIB_LIBRARIES", self.spec["zlib-api"].libs),
                ]
            )

            if self.spec.satisfies("+snappy"):
                args.append(self.define("SNAPPY_HOME", self.spec["snappy"].prefix))

        return args
