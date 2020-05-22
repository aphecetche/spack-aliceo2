# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import sys

class Fairmq(CMakePackage):
    """C++ Message Queuing Library and Framework"""

    homepage      = "https://github.com/FairRootGroup/FairMQ"
    url      = "https://github.com/FairRootGroup/FairMQ/archive/v1.3.9.tar.gz"
    git      = "https://github.com/FairRootGroup/FairMQ.git"

    version('1.4.16', sha256='d87885fa65154f0d113a55aa2863c400dc1c0340f211022c5f224d6e078513ba')

    version('1.4.15',
            tag='v1.4.15',
            submodules=True,
            preferred=True,no_cache=True)

    # TODO Once https://github.com/spack/spack/issues/14344 is resolved, enable
    #      source caching again (by removing the `no_cache` argument).

    version('1.4.14', sha256='b6ac5f059bfb7ab63449548a58fb3fa0885a43986d9385dab9b731b0a845a7f1')

    depends_on('boost@1.72.0-alice1: +program_options+filesystem+date_time+regex')
    depends_on('fairlogger')
    depends_on('libzmq')
    depends_on('asiofi')
    depends_on('flatbuffers')
    depends_on('dds',when=(sys.platform!='darwin'))

    depends_on('cmake',type='build')
    depends_on('ninja', type='build')
    depends_on('googletest',type='build')

    generator = 'Ninja'

    conflicts('boost@1.72')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = [
            "-DDISABLE_COLOR=ON",
            "-DBUILD_NANOMSG_TRANSPORT=OFF",
            "-DBUILD_EXAMPLES=ON",
            "-DBoost_NO_BOOST_CMAKE=ON",
            "-DCMAKE_CXX_STANDARD=17"
        ]
        return args
