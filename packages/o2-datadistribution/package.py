# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class O2Datadistribution(CMakePackage):
    """Data Distribution components for the ALICE O2"""

    homepage = "https://github.com/AliceO2Group/DataDistribution/tree/v0.8.0"
    url      = "https://github.com/AliceO2Group/DataDistribution/archive/v0.8.0.tar.gz"

    version('0.8.0', sha256='8f49035cc99632285342f87569614d78f10a9de9c0dcff7ff8afa817c9f1b312')

    depends_on('o2-aliceo2')
    depends_on('ppconsul')
    depends_on('grpc')
    depends_on('o2-monitoring')
    depends_on('spdlog')


    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
