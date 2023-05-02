# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class O2Bookkeeping(CMakePackage):

    homepage = "https://github.com/AliceO2Group/Bookkeeping.git"
    git = "https://github.com/AliceO2Group/Bookkeeping.git"

    version("0.52.0", tag="@aliceo2/bookkeeping@0.52.0")

    variant('cxxstd',default='17',values=('17','20'),multi=False,description="Force a specific C++ standard")

    depends_on("protobuf")
    depends_on("grpc")

    root_cmakelists_dir = 'cxx-client'

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"))
        args.append(self.define("CMAKE_EXPORT_COMPILE_COMMANDS",True))
        return args

