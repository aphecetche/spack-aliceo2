# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os
from shutil import copy

class AliceGridUtils(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://gitlab.cern.ch/jalien/alice-grid-utils/-/archive/0.0.7-patches/alice-grid-utils-0.0.7-patches.tar.gz"

    version('0.0.7-patches', sha256='2bbc4b4e8de366b6ede002c7cdb2129ce0d03afb943e27dd308bc57c8059686d')

    def install(self, spec, prefix):
        os.mkdir(prefix.include)
        path=os.walk('.')
        for root,_,files in path:
            for file in files:
                copy(os.path.join(root,file),prefix.include)
