# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *

from shutil import copytree
import os

class JalienRoot(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://gitlab.cern.ch/jalien/jalien-root"
    url      = "https://gitlab.cern.ch/jalien/jalien-root/-/archive/0.6.x/jalien-root-0.6.x.tar.gz"

    version('0.6.6', sha256='3e40fef387ff9cf95cbcc6fe40aa8161f129c5e45a39fc5ebb9ecade29ceaf0d')

    depends_on('root')
    depends_on('py-xjalienfs')
    depends_on('xrootd')
    depends_on('openssl')

    depends_on('libwebsockets@:3.99.99',type='build')
    depends_on('json-c',type='build')
    depends_on('zlib',type='build')
    depends_on('alice-grid-utils',type='build')

    @run_before('cmake')
    def copy_alice_grid_utils(self):
        copytree(self.spec['alice-grid-utils'].prefix.include,'inc',dirs_exist_ok=True)
   
    def setup_build_environment(self,env): 
        if "platform=darwin" in self.spec:
            env.unset("MACOSX_DEPLOYMENT_TARGET")

    def setup_run_environment(self,env): 
        env.set('ROOT_PLUGIN_PATH',os.path.join(self.prefix,'etc','plugins'))
        env.set('ROOT_INCLUDE_PATH',os.path.join(self.prefix,'include'))

    # def setup_dependent_build_environment(self, env, dependent_spec):
    #     self.setup_run_environment(env)

    def cmake_args(self):
        args = []
        return args
