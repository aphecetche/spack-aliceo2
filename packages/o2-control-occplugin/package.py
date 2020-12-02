# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class O2ControlOccplugin(CMakePackage):
    """Alice O2 Control and Configuration (OCC)"""

    homepage = "https://github.com/AliceO2Group/Control"
    url = "https://github.com/AliceO2Group/Control/archive/v0.13.92.tar.gz"
    git = "https://github.com/AliceO2Group/Control.git"

    root_cmakelists_dir = 'occ'

    version('0.18.2',
            sha256='86120e190651f697f9b92b63361d385fdc95e9b6bc0bdb8893823012515a2af0')
    version('0.18.1',
            sha256='81cf31b3e4dd76546181f7db1de8a6f598786bb57420231f265c6023e5007d93')
    version('0.18.0',
            sha256='79ada6a5e63446be5e0ed2d21f899ccb2f112807cee3ff170766db197fef0249',
            preferred=True)
    version('0.13.92', sha256='19d62f20da0d07d05356c12ed8216c6c321ff6059b14bf0ba6571edaa2eb03b6')
    version('0.13.91', sha256='899442f175ed2bac4020e45ea35e431991adee4d6d33b2d17402d4f74f1b6d9a')
    version('0.13.90', sha256='94acd278a98632289e291826379d679de3daff288bd6c3666f6744983c1d5fc2')
    version('0.13.3',
            sha256='1094767866330cb0158d9ba5af59dcb248dd0cb8f7e046aaec0cf46504af04d2')

    depends_on('fairmq')
    depends_on('fairlogger')
    depends_on('boost')
    depends_on('protobuf')
    depends_on('openssl')
    depends_on('o2-infologger+libonly')
    depends_on('o2-configuration')
    depends_on('fmt')
    depends_on('abseil-cpp')
    depends_on('grpc')
    depends_on('rapidjson')

    depends_on('cmake', type='build')
    depends_on('ninja', type='build')

    generator = 'Ninja'

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = [
            "-DBUILD_SHARED_LIBS=ON"
        ]
        return args
