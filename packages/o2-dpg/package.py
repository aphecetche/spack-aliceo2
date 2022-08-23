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
#     spack install o2-dpg
#
# You can edit this file again by typing:
#
#     spack edit o2-dpg
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os
from shutil import copytree

class O2Dpg(Package):
    """scripts and configurations to run Monte Carlo simulations and data
    reconstruction of the ALICE experiment within the O2 project."""

    homepage = "https://github.com/AliceO2Group/O2DPG"
    git = "https://github.com/AliceO2Group/O2DPG.git"
    url = "https://github.com/AliceO2Group/O2DPG/archive/refs/tags/20220203.tar.gz"
    #url = "https://github.com/AliceO2Group/O2DPG/archive/refs/tags/prod-202107-22.tar.gz"

    version("master",branch="master")

    version('epn-20220203', sha256='9ef98951884237a903e7f40083abaf1c37906962fe53f5918527265e0316f4aa')
    version('20220201-1146', sha256='ae6c4a5275a855fd89ae5d3eee1ca5bafbed04e689b4e7d90673d727d79d32ce')
    version('202107-22', sha256='b12ea55fa568818055aa2dad5efda02b8df4a27613ed9cd51bc60d1924cf3712')

    depends_on("coreutils")
    depends_on("o2-qualitycontrol")

    def install(self, spec, prefix):
        copytree('.',prefix,dirs_exist_ok=True)

    def setup_environment(self,spack_env,run_env):
        run_env.set('O2DPG_ROOT',self.prefix)
