# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install aegis
#
# You can edit this file again by typing:
#
#     spack edit aegis
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class O2Aegis(CMakePackage):
    """ ALICE Event-Generator Interface for Simulation (AEGISo2).
    AEGISo2 is the framework used by the ALICE experiment to interface Monte
    Carlo event generators with the ALICEo2 simluation framework."""

    homepage = "https://github.com/AliceO2Group/AEGIS/"
    url      = "https://github.com/AliceO2Group/AEGIS/archive/refs/tags/v1.4.tar.gz"


    version('1.4', sha256='14238e5eb128dd817013001bcce51470b08818a647477755055d9bc5fbc84947')

    depends_on('root+pythia6+pythia8~vmc')
    depends_on('pythia6')
    depends_on('hijing')
    depends_on('vmc')

    def cmake_args(self):
        args = []
        args.append(self.define("CMAKE_Fortran_FLAGS","-fallow-argument-mismatch"))
        return args

    def patch(self):
        filter_file('\${ROOT_LIBRARIES}','PUBLIC ROOT::VMC','GeneratorCosmics/CMakeLists.txt')
        filter_file('find_package\(ROOT REQUIRED COMPONENTS EG\)','find_package(ROOT REQUIRED COMPONENTS EG)\nfind_package(VMC)\n','GeneratorCosmics/CMakeLists.txt')
        filter_file('\${ROOT_LIBRARIES}','PUBLIC ROOT::VMC','GeneratorParam/CMakeLists.txt')
        filter_file('find_package\(ROOT REQUIRED COMPONENTS EG\)','find_package(ROOT REQUIRED COMPONENTS EG)\nfind_package(VMC)\n','GeneratorParam/CMakeLists.txt')
