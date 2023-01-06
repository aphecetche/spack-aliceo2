# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
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
#     spack install o2-itsresponse
#
# You can edit this file again by typing:
#
#     spack edit o2-itsresponse
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
import os

class O2Itsresponse(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/AliceO2Group/ITSChipResponseData/archive/refs/tags/v1.0.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]

    version("1.0.0", sha256="08c8303f346131d32e1ae24c3cff0b7b9cd1f8bd856c68d7d9b61376154148ea")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def setup_run_environment(self,env):
        env.set("ITSRESPONSE_ROOT",prefix)

    def setup_build_environment(self,env):
        env.set("ITSRESPONSE_ROOT",prefix)

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        dest = os.path.join(self.prefix,"response")
        os.mkdir(dest)
        path = os.walk(".")
        for root, directories, files in path:
                for file in files:
                    copy(os.path.join(root,file),dest)
