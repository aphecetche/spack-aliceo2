# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import sys

class Libjalieno2(CMakePackage):
    """JAliEn interface library for O2
    This library manages client's credentials and decorates SSL context with
    JAliEn-specific information"""

    homepage = "https://gitlab.cern.ch/jalien/libjalieno2"
    url      = "https://gitlab.cern.ch/jalien/libjalieno2/-/archive/0.1.3/libjalieno2-0.1.3.tar.gz"
    git = "https://gitlab.cern.ch/jalien/libjalieno2.git"

    version('0.1.3', sha256='962d8350ea7da58294034392c04525c89d75eb3fde469d126150b74a76390b8f')

    depends_on('openssl')
    #depends_on('alien')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        args.append(self.define("OPENSSL_ROOT_DIR",self.spec["openssl"].prefix))
        return args
