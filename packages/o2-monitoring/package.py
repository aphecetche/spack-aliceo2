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
#     spack install monitoring
#
# You can edit this file again by typing:
#
#     spack edit monitoring
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class O2Monitoring(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/AliceO2Group/Monitoring"
    url = "https://github.com/AliceO2Group/Monitoring/archive/v3.0.7.tar.gz"
    git = "https://github.com/AliceO2Group/Monitoring.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('3.10.1', sha256='2ce9a3555f59846427d0421208c8eee1fac1532f3b13adda55cf4fd570d2a98e')
    version('3.9.0', sha256='3ad0a301b90f18116690f3475ebab88971c797e702b96fa116ed988fa5e657ed')
    version('3.8.11', sha256='ba9c4db113208627708ab098c41e50a85bb68f045e4665ec8f15eea8696a6869')
    version('3.8.10', sha256='dfe7e834c81896bc44c4f0d44422ec9d975e15967858584b0e19aef8944e98eb')
    version('3.8.9', sha256='62a554b3b4a5de792999d0948ce91d53c55447062f667e8501330ab34c665d0c')
    version('3.8.7', sha256='744ee0764460b89a3710456f5da20cf08471c5e3608d6e32d447920c83ce0f4f')
    version('3.8.6', sha256='327c4d018e59c541f062d4d3e53f21d0cce51bf870ca5603ebeb44d2401fcd3c')
    version('3.8.5', sha256='44650e25b90311cd3741757614e8421f27b5e7a771c4b6486f8dc7c22e72ed2e')
    version('3.8.4', sha256='56dfd6fd12575b4efd53797ce825a6e3bfa9f4d2a6dd70345c07cf1b433bf92b')
    version('3.4.0', sha256='648d4c73d4794ee5b1763b2b574c357fcf9ea7e44c980f4aaeeee2edca6084b7')
    version('3.1.0', sha256='bec5ce7e809cc4ac08e524da8dde6f1967170488a7d27b5fe4fb2a41330ebedb')

    # FIXME: Add dependencies if required.
    depends_on('apmon-cpp')
    depends_on('boost')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
