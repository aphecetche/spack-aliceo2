# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import sys
import platform


class Ppconsul(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    url = "https://github.com/oliora/ppconsul/archive/v0.2.1.tar.gz"
    git = "https://github.com/oliora/ppconsul.git"
    homepage = "https://github.com/oliora/ppconsul"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version(
        '0.2.1', sha256='31f3f23d56eed7e7e35b512ba7caca14185d073a7eb81ade832b4b9a2c4ce1c7')
    version(
        '0.2',   sha256='f4d8217381ae44b7da83b3970922ec0a651093098555871b5a39076a246e7906')
    version(
        '0.1',   sha256='f27ac427b75751881b8ffa1629603a3c10aa6a4d09ad94bb7c4fe6c29069f0ee')

    # FIXME: Add dependencies if required.
    depends_on('boost')
    depends_on('curl')

    generator('ninja')

    def cmake_args(self):
        args = [self.define("BUILD_SHARED_LIBS", True)]
        if sys.platform == 'darwin' and platform.machine() == 'arm64':
            # disable tests on Apple M1 as the ppbconsul internal Catch
            # framework does not compile (and did not have time to investigate
            # why)
            args.append(self.define("BUILD_TESTS", False))
        return args
