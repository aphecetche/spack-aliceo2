# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os

#
# A Fake Package to provide a fake brew command that internally
# calls Spack to location packages...
#
# (meant as an adapter for alibuild recipes which uses the brew command)
#

class FakeBrew(BundlePackage):
    """FIXME: Put a proper description of your package here."""

    phases = ['install']

    version('1.0.0')

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(os.path.join(self.package_dir,'brew'),os.path.join(prefix.bin,'brew'))
