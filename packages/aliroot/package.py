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
#     spack install aliroot
#
# You can edit this file again by typing:
#
#     spack edit aliroot
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Aliroot(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/alisw/AliRoot/archive/refs/tags/v5-09-38k.tar.gz"

    version('5-09-58b', sha256='f232372df319ba770d58d94e0afaf6eb499f3c5b833eed5a16f1f5aedb86ae77')

    depends_on('root~vmc')
    depends_on('vmc')
    depends_on('geant3')
    depends_on('geant4-vmc')
    depends_on('vc')
    depends_on('ninja',type='build')

    def cmake_args(self):
        args = []
        args.append(self.define("CMAKE_EXPORT_COMPILE_COMMANDS",True))
        args.append(self.define("ROOTSYS",self.spec['root'].prefix))
        args.append(self.define("CMAKE_CXX_STANDARD",'17'))
        args.append(self.define("CMAKE_GENERATOR","Ninja"))
        return args
