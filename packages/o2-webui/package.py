# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
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
#     spack install o2-webui
#
# You can edit this file again by typing:
#
#     spack edit o2-webui
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class O2Webui(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/AliceO2Group/WebUi/archive/refs/tags/@aliceo2/web-ui@1.21.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2', sha256='ebdcc4a66e7e360908075db74d106c6e700fe5345fa66b4408e57a1ec44e1d82')

    # FIXME: Add dependencies if required.
    #depends_on('node-js')
    depends_on("cairo",type=("build"))
    depends_on("pixman",type=("build"))
    depends_on("pkgconfig",type=("build"))

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        npm('install')
        # make()
        # make('install')
