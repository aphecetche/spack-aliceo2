# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class O2Infologger(CMakePackage):
    """AliceO2 logging library"""

    homepage = "https://github.com/AliceO2Group/InfoLogger"
    url = "https://github.com/AliceO2Group/InfoLogger/archive/v1.3.9.tar.gz"
    git = "https://github.com/AliceO2Group/InfoLogger.git"

    variant('libonly', default=True, description='Builds only the library')

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('master', branch='master')
    version('2.2.0', sha256='04eea3ca40e562bddd1b442a999acd3487d0749e2200a967a7d7a98f2c64ad5e')
    version('2.1.1', sha256='418c2d582117f9d9dc7a2d5c5b4b1c3190542bd565954b1bbba434cd6649f764')
    version('2.1.0', sha256='709a19aa25e5557d91c37abdf721d5b559bf550304925e9620878f6f9143e497')

    version('2.0.1', sha256='e2fc85d80b3ee3189e962da02c872eff68c944c989d0820d3c4059b084574c5a')
    version('1.3.16', sha256='b9949769678e8a1ff9a84630432fff53400c9910b5415a05e4c61fb0bada62de')
    version('1.3.9', '350dbe5bd8d0a121e53828b79341487b')

    depends_on('boost +container cxxstd=17')
    depends_on('mariadb-client', when='-libonly')
    depends_on('swig', when='-libonly', type='build')
    depends_on('go', when='-libonly', type='build')
    depends_on('cmake', type='build')
    depends_on('ninja', type='build')

    generator = 'Ninja'

    def cmake_args(self):
        args = ['-DINFOLOGGER_BUILD_LIBONLY=%d' %
                (1 if '+libonly' in self.spec else 0)]
        return args
