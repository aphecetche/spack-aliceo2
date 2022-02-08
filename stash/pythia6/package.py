# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Pythia6(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/alisw/pythia6/archive/refs/tags/428-alice2.tar.gz"

    version('428-alice2', sha256='e3688915a0abdda52d866860c4d0db3101e403271153a6c0c926fc0d3eceb09c')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def cmake_args(self):
        args = []
        args.append('-DCMAKE_MACOSX_RPATH=ON')
        return args
