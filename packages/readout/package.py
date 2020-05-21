# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Readout(CMakePackage):
    """AliceO2 Readout Package"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage      = "https://github.com/AliceO2Group/Readout.git"
    url      = "https://github.com/AliceO2Group/Readout/archive/v1.3.10.2.RDH6.tar.gz"
    git      = "https://github.com/AliceO2Group/Readout.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.3.10.1.RDH6', sha256='ad1a2882c6a47e3ed5f5fdd1d52a85f6305217f820da5c2d806793da25c3d57d')
    version('1.3.10.2.RDH6', sha256='f12a59ba7ce00c17812ff2f1667d1f2ddb3dd52139a113e5dd7c6ec9051dc913')
    version('1.3.10',
            sha256='97399aad0809c64fbd0bb3b7906a14eec13ee7557c5667d9abb401a73956a52f',
            preferred=True)

    depends_on('boost')
    depends_on('aliceo2.common')
    depends_on('aliceo2.infologger+libonly')
    depends_on('aliceo2.monitoring')
    depends_on('aliceo2.configuration')
    depends_on('aliceo2.readoutcard')
    depends_on('fairlogger')
    depends_on('fairmq')
    depends_on('lz4')
    depends_on('control-occplugin')

    depends_on('cmake',type='build')
    depends_on('ninja', type='build')
    generator = 'Ninja'

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
