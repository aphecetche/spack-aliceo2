# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class O2Debuggui(CMakePackage):
    """Standalone utility package for DPL Debug GUI"""

    homepage = "https://github.com/AliceO2Group/DebugGUI"
    url      = "https://github.com/AliceO2Group/DebugGUI/archive/refs/tags/v0.6.1.tar.gz"

    version("0.8.0", sha256="c7b7c38023328f40628b37b34551d4fc2bb306345d5f0a93880317581954c5b8")
    version("0.7.2", sha256="c52c398a9e37ae34c8afeb3f2c3fff4c164505312b7008c63b43622b636c30fb")
    version("0.7.1", sha256="d0f99a402cee9ca512954a576d1080f83b3b27b703ee40568ebaa2824643a236")
    version("0.7.0", sha256="61e72849c93956ad90d062c7f907f6d982cc88343c97b9380483542fd4533cdb")
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
