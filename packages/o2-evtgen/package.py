# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class O2Evtgen(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/alisw/EVTGEN"
    url ="https://github.com/alisw/EVTGEN/archive/refs/tags/R02-02-00.tar.gz"

    version("02-02-00", sha256="a79fe1ad794d11b0c2a1e74522556f80f3f4f2747d37b17d3a2ff01f12e103aa")

    depends_on('hepmc')
    depends_on('pythia8')
    depends_on('tauola +lhapdf')
    depends_on('photos')

    def cmake_args(self):
        args = []
        return args

    def setup_run_environment(self,env):
      env.set('EVTGEN_ROOT',self.prefix)
      env.append_path('ROOT_INCLUDE_PATH',self.prefix.include)
      env.append_path('ROOT_DYN_PATH',self.prefix.lib)

