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
    depends_on('kfparticle')
    depends_on('ninja',type='build')
    depends_on('pkgconfig',type='build')
    depends_on('fjcontrib')

    def cmake_args(self):
        args = []
        args.append(self.define("CMAKE_EXPORT_COMPILE_COMMANDS",True))
        return args

    def setup_build_environment(self,env):
        if self.spec.satisfies("platform=darwin"):
            env.unset("MACOSX_DEPLOYMENT_TARGET")
