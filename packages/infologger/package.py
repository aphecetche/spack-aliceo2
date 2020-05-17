# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Infologger(CMakePackage):
    """AliceO2 logging library"""

    homepage = "https://github.com/AliceO2Group/InfoLogger"
    git = "https://github.com/AliceO2Group/InfoLogger.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('master',branch='master') 

    depends_on('cmake','type=build')
    depends_on('boost')

    def cmake_args(self):
        args = ['-DINFOLOGGER_BUILD_LIBONLY=1']
        return args
