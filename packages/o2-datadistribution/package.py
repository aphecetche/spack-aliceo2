# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class O2Datadistribution(CMakePackage):
    """Data Distribution components for the ALICE O2"""

    homepage = "https://github.com/AliceO2Group/DataDistribution/tree/v0.8.0"
    url      = "https://github.com/AliceO2Group/DataDistribution/archive/v0.8.0.tar.gz"

    version('1.0.10', sha256='a3986411c0cfbf6acabe26798251fd80d1302495301660d3eddae2f90b86b69d')
    version('1.0.9', sha256='a9675936b8212285399f3ede3a1a19e94cf34889a36cf6e7c5bb503351fead49')
    version('1.0.8', sha256='8d26162fc97d24986b0fd097617c858e494a71cf32df9d16ae6de53568786a8c')
    version('1.0.7', sha256='0b2f15a0216a355cf3f8a0651b514699f0d928ab34143007f563cbe64c7bf4fe')
    version('1.0.6', sha256='6c2297391014b0b0036542d4c9430446b837472a9eba919f38c33a1a41190527')

    version('0.8.0', sha256='8f49035cc99632285342f87569614d78f10a9de9c0dcff7ff8afa817c9f1b312')

    depends_on('o2-aliceo2')
    depends_on('ppconsul')
    depends_on('grpc')
    depends_on('o2-monitoring')
    depends_on('spdlog')
    depends_on('autoconf',type='build')
    depends_on('automake',type='build')
    depends_on('libtool',type='build')
    depends_on('m4',type='build')


    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
