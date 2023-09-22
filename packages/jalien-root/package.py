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

    version("0.7.3", sha256="4521fd4243c741abcf6e4bddf4a16649c2be34b3f21e3e69067a1f0706f73d62")
    version("0.7.1", sha256="9c046d90d7f4d13dd83e8e1ac03f89e0c92e5c742e9e158027a69d6708abaf73")
    version("0.6.9", sha256="6080525acc64352485e2eb39f590d1a16a8a700679dc48ed63b22940ccd087a2")
    version("0.6.8", sha256="38001924536a9fc95ae8bb8bc8d5b839ad594bec0d32107ed32d330480d69062")
    version('0.6.6', sha256='3e40fef387ff9cf95cbcc6fe40aa8161f129c5e45a39fc5ebb9ecade29ceaf0d')

# find_package(JSONC REQUIRED)
# find_package(OpenSSL REQUIRED)
# find_package(libwebsockets REQUIRED)
# find_package(ROOT REQUIRED COMPONENTS Net NetxNG Tree XMLIO)
# find_package(ZLIB REQUIRED)
# find_package(XROOTD REQUIRED)

    depends_on('root +xrootd +xml')
    depends_on('py-xjalienfs')
    #depends_on('xrootd')
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
        env.append_path('ROOT_DYN_PATH',self.prefix.lib)
        env.prepend_path('ROOT_PLUGIN_PATH',os.path.join(self.prefix,'etc','plugins'))
        env.prepend_path('ROOT_INCLUDE_PATH',self.prefix.include)

    def cmake_args(self):
        args = []
        return args
