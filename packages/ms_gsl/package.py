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
#     spack install gsl
#
# You can edit this file again by typing:
#
#     spack edit gsl
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class MsGsl(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/microsoft/GSL/archive/v3.1.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('3.1.0', sha256='d3234d7f94cea4389e3ca70619b82e8fb4c2f33bb3a070799f1e18eef500a083')
    version('3.0.1', sha256='7ceba191e046e5347357c6b605f53e6bed069c974aeda851254cb6962a233572')
    version('3.0.0', sha256='767b6246eecd0b2a915e2b5774ba6d4796579a5e15dc562d93ec80f1f2c9c889')
    version('2.1.0', sha256='ef73814657b073e1be86c8f7353718771bf4149b482b6cb54f99e79b23ff899d')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
