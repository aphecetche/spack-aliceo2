# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Utf8proc(CMakePackage):
    """A clean C library for processing UTF-8 Unicode data:
    normalization, case-folding, graphemes, and more"""

    homepage = "https://juliastrings.github.io/utf8proc/"
    url      = "https://github.com/JuliaStrings/utf8proc/archive/v2.4.0.tar.gz"

    version('2.5.0', sha256='d4e8dfc898cfd062493cb7f42d95d70ccdd3a4cd4d90bec0c71b47cca688f1be')
    version('2.4.0', sha256='b2e5d547c1d94762a6d03a7e05cea46092aab68636460ff8648f1295e2cdfbd7')

    variant('shared', default=True, description='Build a shared version of the library')

    depends_on('cmake@2.8.12:', type='build')

    def cmake_args(self):
      args = []
      args.append(self.define_from_variant("BUILD_SHARED_LIBS","shared"))
      return args
