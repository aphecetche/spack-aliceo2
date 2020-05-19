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
#     spack install apmon-cpp
#
# You can edit this file again by typing:
#
#     spack edit apmon-cpp
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import sys

class ApmonCpp(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/alisw/apmon-cpp.git"
    url      = "https://github.com/alisw/apmon-cpp/archive/v2.2.8-alice5.tar.gz"
    git = "https://github.com/alisw/apmon-cpp.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2.2.8-alice5', sha256='ebf5b60b1cb72a9857a1d16fd1fbec281ac30906c2898441f1dd2dd1bb51a109')
    version('2.2.8-alice4', sha256='6b35a8d980831356774601a3ab04661e8ec0f804fcb58d5441bd5c687d853530')
    version('2.2.8-alice3', sha256='149f5855da45b278945c0636590e0c824bb5d73d3d78c86ccd0d589d0ccadf8f')

    # FIXME: Add dependencies if required.
    depends_on('libtirpc',when=(sys.platform != 'darwin'))

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
