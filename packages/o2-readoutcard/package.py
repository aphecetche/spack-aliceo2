# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import sys
import os

class O2Readoutcard(CMakePackage):
    """AliceO2 ReadoutCard module"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage      = "https://github.com/AliceO2Group/ReadoutCard.git"
    url      = "https://github.com/AliceO2Group/ReadoutCard/archive/v0.21.1.tar.gz"
    git      = "https://github.com/AliceO2Group/ReadoutCard.git"
    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.32.3', sha256='6859cadc431abedd3035deba1298f12fa952bee45b2830555549154577d15115')
    version('0.26.0', sha256='5ffe927559fb345851e5ef99eb644e65f09851f2ec635371cb99137042ddec75')
    version('0.21.1', sha256='cf918d1960d5657ac36e448357b94c5ec9d37a38725a27ecd787bfca494c28ad')

    # FIXME: Add dependencies if required.
    depends_on('pda',when=(os=='slc'))

    depends_on('boost')
    depends_on('o2-monitoring')
    depends_on('o2-common')
    depends_on('o2-configuration')
    depends_on('o2-infologger+libonly')

    depends_on('cmake',type='build')
    depends_on('ninja', type='build')

    generator = 'Ninja'

    def cmake_args(self):
        args = [ "-DBUILD_SHARED_LIBS=ON" ]
        return args
