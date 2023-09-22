# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Aliphysics(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/alisw/AliPhysics"
    git = "https://github.com/alisw/AliPhysics.git"
    url = "https://github.com/alisw/AliPhysics/archive/refs/tags/vAN-20211130.tar.gz"
    generator('ninja')

    version('vAN-20211130',
            sha256='3834cbe8295fc8d8c7161aa6459f79fb1eac6486271a5245adc45340c446455d')

    depends_on('fastjet')
    depends_on('fjcontrib')
    depends_on('kfparticle')
    depends_on('aliroot')
    depends_on('treelite')
    # should not be necessary if aliroot used proper CMake targets...
    depends_on('vmc')

    def cmake_args(self):
        args = []
        args.append(self.define("ALIROOT", self.spec['aliroot'].prefix))
        args.append(self.define("TREELITE_ROOT", self.spec['treelite'].prefix))
        args.append(self.define("KFPARTICLE", self.spec['kfparticle'].prefix))
        args.append(self.define("ROOTSYS", self.spec['root'].prefix))
        args.append(self.define("CMAKE_EXPORT_COMPILE_COMMANDS", True))
        args.append(self.define("CMAKE_CXX_STANDARD", '17'))
        return args
