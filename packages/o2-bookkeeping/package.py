# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class O2Bookkeeping(CMakePackage):

    homepage = "https://github.com/AliceO2Group/Bookkeeping.git"
    url = "https://github.com/AliceO2Group/Bookkeeping/releases/download/%40aliceo2%2Fbookkeeping%400.52.0/aliceo2-bookkeeping-0.52.0.tgz"

    version("0.52.0", sha256="94ec9e0e7c910ca5af846231181dbbb207cae21e95540a771ab5b85c1774e638")

    variant('cxxstd',default='17',values=('17','20'),multi=False,description="Force a specific C++ standard")

    root_cmakelists_dir = 'src'

    depends_on("protobuf")
    depends_on("grpc")

    root_cmakelists_dir = 'cxx-client'

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"))
        args.append(self.define("CMAKE_EXPORT_COMPILE_COMMANDS",True))
        return args

