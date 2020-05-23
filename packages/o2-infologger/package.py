# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class O2Infologger(CMakePackage):
    """AliceO2 logging library"""

    homepage = "https://github.com/AliceO2Group/InfoLogger"
    url="https://github.com/AliceO2Group/InfoLogger/archive/v1.3.9.tar.gz"
    git = "https://github.com/AliceO2Group/InfoLogger.git"

    variant('libonly',default=True,description='Builds only the library')

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('master',branch='master') 
    version('1.3.9','350dbe5bd8d0a121e53828b79341487b')

    depends_on('boost')
    depends_on('mariadb-client',when='-libonly')
    depends_on('swig',when='-libonly',type='build')
    depends_on('go',when='-libonly',type='build')
    depends_on('cmake',type='build')
    depends_on('ninja', type='build')

    generator = 'Ninja'

    def cmake_args(self):
        args = ['-DINFOLOGGER_BUILD_LIBONLY=%d' % (1 if '+libonly' in self.spec else 0)]
        return args
