# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class O2Debuggui(CMakePackage):
    """Standalone utility package for DPL Debug GUI"""

    homepage = "https://github.com/AliceO2Group/DebugGUI"
    url      = "https://github.com/AliceO2Group/DebugGUI/archive/refs/tags/v0.6.1.tar.gz"

    version('0.6.4', sha256='b212a9463bee36974c6831952c177db9c7a4116cd95b444ace9359cbd2254b06')
    version('0.6.3', sha256='512c6d51b4908a5e544037e045393c5aa945d83d979084622208877498a417f9')
    version('0.6.2', sha256='c5beb47332cf312af00d2a45c3e59d2d5e53cc117c6da6fd3732dfa7fdb50520')
    version('0.6.1', sha256='c9cc4552dbd737d6f5532d8d52347a2ee37a7cdf89a1d4ea35123540f106a08b')

    depends_on('glfw+shared')
    depends_on('freetype')
    depends_on('libuv')
    depends_on('capstone',type='build')

    def cmake_args(self):
        args = []
        return args
