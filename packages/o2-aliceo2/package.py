# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install aliceo2
#
# You can edit this file again by typing:
#
#     spack edit aliceo2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class O2Aliceo2(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/AliceO2Group/AliceO2/archive/v20.49.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('20.49', sha256='f7bda483c4f6666aa6391af470d0bc15c74d4e6aa3632f8e1492496f80ea569f')

    # FIXME: Add dependencies if required.
    depends_on('protobuf')
    depends_on('o2-infologger')
    depends_on('o2-configuration')
    depends_on('o2-monitoring')
    depends_on('o2-common')
    depends_on('rapidjson')
    depends_on('fairroot cxxstd=17',when='+sim')
    depends_on('fairroot~sim cxxstd=17',when='~sim')

    variant('sim',default=False, description='Enable simulation engines and event generators')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        args.append('-DBUILD_SIMULATION=%s' % ( 'ON' if '+sim' in self.spec else 'OFF'))
        return args
