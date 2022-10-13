# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Kfparticle(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/alisw/KFParticle/archive/refs/tags/alice/v1.1-4.tar.gz"


    version('1.1-4', sha256='ab4bedd5c9d5f6ce23d9867e83e7412077dd5d28ed23480c17ef56ccb7ce4429')

    # FIXME: Add dependencies if required.
    depends_on('root')
    depends_on('vc')

    def cmake_args(self):
        args = []
        return args

    def setup_build_environment(self,env):
        if self.spec.satisfies("platform=darwin"):
            env.unset("MACOSX_DEPLOYMENT_TARGET")
