# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class O2Qualitycontrol(CMakePackage):
    """Data Quality Control (QC) software for the ALICE O2 system"""

    homepage = "https://github.com/AliceO2Group/QualityControl"
    url      = "https://github.com/AliceO2Group/QualityControl/archive/v1.10.0.tar.gz"
    git      = "https://github.com/AliceO2Group/QualityControl.git"

    version('master',branch='master')

    version('1.10.0', sha256='3dcdb7330bb5e1b671ad6497eb22d8960894e2b5fecd95976548b06218640293')

    depends_on('o2-aliceo2')
    depends_on('o2-control+occ')

    def cmake_args(self):
        args = []
        return args
