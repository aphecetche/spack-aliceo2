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
#     spack install o2-dataprocessing
#
# You can edit this file again by typing:
#
#     spack edit o2-dataprocessing
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
from shutil import copytree

class O2Dataprocessing(Package):
    """Collection of DPL workflows to be run in production"""

    homepage = "https://github.com/AliceO2Group/O2DataProcessing"
    url      = "https://github.com/AliceO2Group/O2DataProcessing/archive/refs/tags/v0.5.tar.gz"

    version('0.5', sha256='a6a635df977ce80e7b6d1fa963b4a2a976381df0557a80bcaa6b95da2a3c13e6')

    def install(self, spec, prefix):
        copytree('.',prefix,dirs_exist_ok=True)
