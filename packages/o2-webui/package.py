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

    url = "https://github.com/AliceO2Group/WebUi/archive/refs/tags/@aliceo2/web-ui@2.1.0.tar.gz"
    git = "https://github.com/AliceO2Group/WebUI.git"

    version("master",branch="master")
    version("2", sha256="f0181ec4788a02f5cfcd46d1c9821d851deb1c641e03b38fa1fe0836c4df43e5")

    # FIXME: Add dependencies if required.
    #depends_on('node-js')
    depends_on("zlib",type=("build"))
    depends_on("harfbuzz",type=("build"))
    depends_on("gobject-introspection",type=("build"))
    depends_on("pango",type=("build"))
    depends_on("cairo",type=("build"))
    depends_on("pixman",type=("build"))
    depends_on("pkgconfig",type=("build"))
    depends_on("libpng",type=("build"))
    depends_on("python",type=("build"))

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        with working_dir("QualityControl"):
            npm = which("npm")
            npm('install')
        npm('install')
