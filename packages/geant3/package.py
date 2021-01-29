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
#     spack install geant3
#
# You can edit this file again by typing:
#
#     spack edit geant3
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Geant3(CMakePackage):
    """Simulation software using Monte Carlo methods to describe how particles
    pass through matter."""

    homepage = "https://github.com/vmc-project/geant3"
    url      = "https://github.com/vmc-project/geant3/archive/v3-7.tar.gz"

    version('3-7', sha256='36cd57c6e5a54ff11e8687b30f54d774b676e06c55658cbc1ad787d1fadbe509')
    version('3-6', sha256='e2c8f2c8397431218f90e03cafe54aa0de0474536cb9de921573ca670abfd0e0')
    version('3-5', sha256='5bec0b442bbb3456d5cd1751ac9f90f1da48df0fcb7f6bf0a86c566bfc408261')
    version('3-4', sha256='c7b487ab4fb4e6479c652b9b11dcafb686edf35e2f2048045c501e4f5597d62c')

    depends_on('root')

    def cmake_args(self):
        args = []
        if self.satisfies('%gcc10:'):
            args.append('-DCMAKE_Fortran_FLAGS="-fallow-argument-mismatch -fallow-invalid-boz"')
        return args
