# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class O2Readout(CMakePackage):
    """AliceO2 Readout Package"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/AliceO2Group/Readout.git"
    url = "https://github.com/AliceO2Group/Readout/archive/v1.3.10.2.RDH6.tar.gz"
    git = "https://github.com/AliceO2Group/Readout.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version("2.15.2", sha256="84068ef0c20b75d7438f4bbcd5e4cc4af59d553468126b6f98a9bffdcd7d88a8")
    version('2.7.0', sha256='47207c5e7c82d6ecf4de5f8585f6849791eb385c2f1c280045447785ec6b9872')
    version('2.5.2', sha256='91a99faf4df366a8af77dd2a9f12fef00b14aef6145f1312d4cd58b4fd6091e9')
    version('1.5.6',
            sha256='7934ff4965ef44070d4b22f87a42bb0728bfb60a8298c13141d80b8a7a5c9766')
    version('1.5.5',
            sha256='1500442503c949503c0f133b9bd8ccb2cd92f78f979198dfe5bee2a1a9b5bf4f')
    version('1.5.4',
            sha256='9f6c97e56a5d66e2b336693966da97b2ccfd2e7dd0d51437e9a022e2c1e7e2c8')
    version('1.5.3',
            sha256='04622a3d097cbc51eb1cf2bae11f56b70f48e7809f81125df3dd2dce49aa8daf')
    version('1.5.2',
            sha256='5a4d6c52a11f43e5faf5ec528b98eece5915fceaa0645dcb804dd841688ad72e',
            preferred=True)
    version('1.5.1',
            sha256='910f6d6be98388dc7565a2806bb31a614a981f4d7b8b262d6a2f4838a4240ff2')

    version('1.3.10.1.RDH6',
            sha256='ad1a2882c6a47e3ed5f5fdd1d52a85f6305217f820da5c2d806793da25c3d57d')
    version('1.3.10.2.RDH6',
            sha256='f12a59ba7ce00c17812ff2f1667d1f2ddb3dd52139a113e5dd7c6ec9051dc913')
    version('1.3.10',
            sha256='97399aad0809c64fbd0bb3b7906a14eec13ee7557c5667d9abb401a73956a52f')

    depends_on('boost')
    depends_on('o2-common')
    depends_on('o2-infologger+libonly')
    depends_on('o2-monitoring')
    depends_on('o2-configuration')
    depends_on('o2-readoutcard')
    depends_on('fairlogger')
    depends_on('fairmq')
    depends_on('lz4')
    depends_on('o2-control-occplugin')

    depends_on('cmake', type='build')
    depends_on('ninja', type='build')
    generator = 'Ninja'

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
