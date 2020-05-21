# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Configuration(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/AliceO2Group/Configuration"
    url      = "https://github.com/AliceO2Group/Configuration/archive/v2.3.1.tar.gz"
    git      = "https://github.com/AliceO2Group/Configuration.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2.3.1', sha256='66cb9de9461c6cce8af21ea1fb6df1dba5de888aa01694f57749e6ade4a9c7af')

    # FIXME: Add dependencies if required.
    depends_on('curl')
    depends_on('boost')
    depends_on('ppconsul')

    depends_on('cmake',type='build')
    depends_on('ninja', type='build')

    generator = 'Ninja'

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
