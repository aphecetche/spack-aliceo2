# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class O2Aegis(CMakePackage):
    """ ALICE Event-Generator Interface for Simulation (AEGISo2).
    AEGISo2 is the framework used by the ALICE experiment to interface Monte
    Carlo event generators with the ALICEo2 simluation framework."""

    homepage = "https://github.com/AliceO2Group/AEGIS/"
    url      = "https://github.com/AliceO2Group/AEGIS/archive/refs/tags/v1.4.tar.gz"

    variant('cxxstd',default='17',values=('17','20'),multi=False,description="Force a specific C++ standard")
    version('1.4', sha256='14238e5eb128dd817013001bcce51470b08818a647477755055d9bc5fbc84947')

    depends_on('root+pythia6+pythia8~vmc')
    depends_on('pythia6')
    depends_on('hijing')
    depends_on('vmc')

    def cmake_args(self):
        args = []
        args.append(self.define("CMAKE_Fortran_FLAGS","-fallow-argument-mismatch"))
        #args.append(self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"))
        return args

    def patch(self):
        filter_file('\${ROOT_LIBRARIES}','PUBLIC VMCLibrary','GeneratorCosmics/CMakeLists.txt')
        filter_file('find_package\(ROOT REQUIRED COMPONENTS EG\)','find_package(ROOT REQUIRED COMPONENTS EG)\nfind_package(VMC)\n','GeneratorCosmics/CMakeLists.txt')
        filter_file('\${ROOT_LIBRARIES}','PUBLIC VMCLibrary','GeneratorParam/CMakeLists.txt')
        filter_file('find_package\(ROOT REQUIRED COMPONENTS EG\)','find_package(ROOT REQUIRED COMPONENTS EG)\nfind_package(VMC)\n','GeneratorParam/CMakeLists.txt')

    def setup_run_environment(self,env):
        env.set('AEGIS_ROOT',self.prefix)
        env.append_path('ROOT_INCLUDE_PATH', self.prefix.include)
        env.append_path('ROOT_DYN_PATH', self.prefix.lib)

    def setup_build_environment(self,env):
        if "platform=darwin" in self.spec:
            env.unset('MACOSX_DEPLOYMENT_TARGET')

