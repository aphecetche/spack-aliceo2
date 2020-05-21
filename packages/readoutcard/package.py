# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import sys
import os

class Readoutcard(CMakePackage):
    """AliceO2 ReadoutCard module"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage      = "https://github.com/AliceO2Group/ReadoutCard.git"
    url      = "https://github.com/AliceO2Group/ReadoutCard/archive/v0.21.1.tar.gz"
    git      = "https://github.com/AliceO2Group/ReadoutCard.git"
    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.21.1', sha256='cf918d1960d5657ac36e448357b94c5ec9d37a38725a27ecd787bfca494c28ad')

    # FIXME: Add dependencies if required.
    depends_on('pda',when=(os=='slc'))

    depends_on('boost')
    depends_on('aliceo2.monitoring')
    depends_on('aliceo2.common')
    depends_on('aliceo2.configuration')
    depends_on('aliceo2.infologger+libonly')

    depends_on('cmake',type='build')
    depends_on('ninja', type='build')

    generator = 'Ninja'

    def cmake_args(self):
        args = [ "-DBUILD_SHARED_LIBS=ON" ]
        return args
