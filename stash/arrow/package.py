# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from os import path


class Arrow(CMakePackage, CudaPackage):
    """A cross-language development platform for in-memory data.

    This package contains the C++ bindings.
    """

    homepage = "http://arrow.apache.org"
    url = "https://github.com/apache/arrow/archive/apache-arrow-0.9.0.tar.gz"

    version('9.0.0', sha256='bb187b4b0af8dcc027fffed3700a7b891c9f76c9b63ad8925b4afb8257a2bb1b')
    version('6.0.1', sha256='826a7dfb246d47862d43b620e0e579f90a4df4c5e571613651dc6397d1e4a435')
    version('6.0.0', sha256='4e5db56ed20936b84c5b0f8e652528612ad5912fbfeafc3f39ff52a47176165f')
    version('5.0.0', sha256='ec3bdae6ccc08de5b5adcf9cbe7cbc085cab0ba06c8e6d3abfc3ed1cd4c1c9a2')
    version('4.0.1', sha256='79d3e807df4a179cfab1e7a1ab5f79d95f7b72ac2c33aba030febd125d77eb3b')
    version('4.0.0', sha256='a27971e2a71c412ae43d998b7b6d06201c7a3da382c804dcdc4a8126ccbabe67')
    version(
        '3.0.0', sha256='fc461c4f0a60e7470a7c58b28e9344aa8fb0be5cc982e9658970217e084c3a82')
    version(
        '2.0.0', sha256='ea299df9cf440cfc43393ce12ee6d9a4c9d0dfa9fde33c3bc9b70ec25520a844')
    version(
        '1.0.1', sha256='dac59f4d42416224419c020ed2e8f8371e85c1d9ff4368ed5b5c026ee28d3fd4')
    version(
        '1.0.0', sha256='08fbd4c633c08939850d619ca0224c75d7a0526467c721c0838b8aa7efccb270')
    version('0.17.1', sha256='ecb6da20f9288c0ca31f9b457ffdd460198765a8af27c1cac4b1382a8d130f86')
    version('0.15.1', sha256='ab1c0d371a10b615eccfcead71bb79832245d788f4834cc6b278c03c3872d593')
    version('0.15.0', sha256='d1072d8c4bf9166949f4b722a89350a88b7c8912f51642a5d52283448acdfd58')
    version('0.14.1', sha256='69d9de9ec60a3080543b28a5334dbaf892ca34235b8bd8f8c1c01a33253926c1')
    version('0.12.1', sha256='aae68622edc3dcadaa16b2d25ae3f00290d5233100321993427b03bcf5b1dd3b')
    version('0.11.0', sha256='0ac629a7775d86108e403eb66d9f1a3d3bdd6b3a497a86228aa4e8143364b7cc')
    version(
        '0.9.0', sha256='65f89a3910b6df02ac71e4d4283db9b02c5b3f1e627346c7b6a5982ae994af91')
    version(
        '0.8.0', sha256='c61a60c298c30546fc0b418a35be66ef330fb81b06c49928acca7f1a34671d54')

    depends_on('boost@1.60:')
    depends_on('cmake@3.2.0:', type='build')
    depends_on('flatbuffers')
    depends_on('llvm+clang', when='+gandiva',type='build')
    depends_on('openssl',when='+gandiva @6.0.0:')
    depends_on('lz4', when='+lz4')
    depends_on('ninja', type='build')
    depends_on('orc', when='+orc')
    depends_on('protobuf', when='+gandiva')
    depends_on('py-numpy', when='+python')
    depends_on('python', when='+python')
    depends_on('rapidjson')
    depends_on('re2+shared', when='+gandiva')
    depends_on('snappy~shared', when='+snappy')
    depends_on('thrift+pic', when='+parquet')
    depends_on('utf8proc')
    depends_on('zlib+pic', when='+zlib')
    # depends_on('zstd+pic', when='+zstd')
    depends_on('zstd', when='+zstd')
    depends_on('openssl',when='@4.0.0:')
    depends_on('xsimd',when='@9.0.0:')

    variant('brotli', default=False, description='Build support for Brotli compression')
    variant('build_type', default='Release', description='CMake build type', values=('Debug', 'FastDebug', 'Release'))
    variant('compute', default=True, description='Computational kernel functions and other support')
    variant('cxxstd',default='11',values=('11','17'),multi=False,description='Require a specific C++ standard')
    variant('gandiva', default=True, description='Build Gandiva support')
    variant('glog', default=False, description='Build libraries with glog support for pluggable logging')
    variant('hdfs', default=False, description='Integration with libhdfs for accessing the Hadoop Filesystem')
    variant('ipc', default=True, description='Build the Arrow IPC extensions')
    variant('jemalloc', default=False, description='Build the Arrow jemalloc-based allocator')
    variant('lz4', default=True, description='Build support for lz4 compression')
    variant('orc', default=False, description='Build integration with Apache ORC')
    variant('parquet', default=False, description='Build Parquet interface')
    variant('python', default=False, description='Build Python interface')
    variant('shared', default=True, description='Build shared libs')
    variant('snappy', default=False, description='Build support for Snappy compression')
    variant('tensorflow', default=False, description='Build Arrow with TensorFlow support enabled')
    variant('zlib', default=True, description='Build support for zlib (gzip) compression')
    variant('zstd', default=False, description='Build support for ZSTD compression')

    root_cmakelists_dir = 'cpp'

    def patch(self):
        """Prevent `-isystem /usr/include` from appearing, since this confuses gcc.
        """
        filter_file(r'(include_directories\()SYSTEM ',
                    r'\1',
                    'cpp/cmake_modules/ThirdpartyToolchain.cmake')

        filter_file(r'set\(ARROW_LLVM_VERSIONS "10" "9" "8" "7"\)',
                    'set(ARROW_LLVM_VERSIONS "11" "10" "9" "8" "7")',
                    'cpp/CMakeLists.txt', when='@:2.0.0')

        filter_file(r'#include <llvm/Support/DynamicLibrary\.h>',
                    r'#include <llvm/Support/DynamicLibrary.h>' +
                    '\n' + r'#include <llvm/Support/Host.h>',
                    'cpp/src/gandiva/engine.cc', when='@2.0.0')

    def cmake_args(self):
        args = [
            '-DARROW_DEPENDENCY_SOURCE=SYSTEM',
            '-DARROW_NO_DEPRECATED_API=ON'
        ]

        if self.spec.satisfies('+shared'):
            args.append(self.define('BUILD_SHARED','ON'))
        else:
            args.append(self.define('BUILD_SHARED','OFF'))
            args.append(self.define('BUILD_STATIC','ON'))

        if self.spec.satisfies('@:0.11.99'):
            # ARROW_USE_SSE was removed in 0.12
            # see https://issues.apache.org/jira/browse/ARROW-3844
            args.append(self.define('ARROW_USE_SSE','ON'))

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

        return args
