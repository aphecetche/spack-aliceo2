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

    version('3.4.0',
            sha256='648d4c73d4794ee5b1763b2b574c357fcf9ea7e44c980f4aaeeee2edca6084b7')
    version(
        '3.1.0', sha256='bec5ce7e809cc4ac08e524da8dde6f1967170488a7d27b5fe4fb2a41330ebedb')

    # FIXME: Add dependencies if required.
    depends_on('apmon-cpp')
    depends_on('boost')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
