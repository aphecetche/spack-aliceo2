# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class O2Configuration(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/AliceO2Group/Configuration"
    url      = "https://github.com/AliceO2Group/Configuration/archive/v2.3.1.tar.gz"
    git      = "https://github.com/AliceO2Group/Configuration.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2.6.3', sha256='23fc82d2abc43eee3440f729e97d5f54b9054680bb03be39b30784938c9ccb8c')
    version('2.6.2', sha256='815eed1c00ffe339bd6237d69da53416ca29183308486979c166f9271887c491')
    version('2.6.1', sha256='16bc3b56254d23431cabfaebb775a00061531a99370f2c40a6569571d1742a65')
    version('2.5.0', sha256='8a1be54bbc59dd85248d0a986da3324ea2fac74a7f5c634f8495e3c86df01657')
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
