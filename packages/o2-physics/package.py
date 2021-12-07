# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os

class O2Physics(CMakePackage):
    """ALICE O2 Analysis repository."""

    homepage = "https://github.com/AliceO2Group/O2Physics"
    url      = "https://github.com/AliceO2Group/O2Physics/archive/refs/tags/nightly-20210818.tar.gz"
    git = "https://github.com/AliceO2Group/O2Physics.git"

    version('master',branch='master')
    version('20210818', sha256='c18355232b6f9f7256751d657a8b862521e68473243328589b51ba82cd53b410')

    generator = 'Ninja'

    depends_on('o2-aliceo2+sim+analysis')
    depends_on('onnxruntime')
    depends_on('ninja',type='build')
    depends_on('pkg-config',type='build')
    depends_on('fjcontrib')

    @run_before('cmake')
    def copy_find_onnxruntime(self):
        copy(os.path.join(os.path.dirname(__file__),'FindONNXRuntime::ONNXRuntime.cmake'),'cmake/FindONNXRuntime::ONNXRuntime.cmake')
        copy(os.path.join(os.path.dirname(__file__),'Findfjcontrib.cmake'),'cmake/Findfjcontrib.cmake')

    def patch(self):
       filter_file(r'find_package\(O2 CONFIG REQUIRED\)',
       '\n' + 'find_package(O2 CONFIG REQUIRED)' + 
       '\n' + 'find_package(fjcontrib REQUIRED)',
       'CMakeLists.txt')
       filter_file(r'find_package\(ONNXRuntime::ONNXRuntime CONFIG REQUIRED\)',
       '\n' + 'find_package(ONNXRuntime::ONNXRuntime REQUIRED)',
       'CMakeLists.txt')

    def cmake_args(self):
        args = []
        args.append(self.define("CMAKE_EXPORT_COMPILE_COMMANDS",True))
        args.append(self.define("fjcontrib_ROOT",self.spec["fjcontrib"].prefix))
        return args
