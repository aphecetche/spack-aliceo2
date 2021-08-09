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

    version('1.24.1', sha256='4b87c3301e3c201807b0e42385bfee722e77130d99eef39d92e1681918c830df')
    version('1.18.1', sha256='4dfb8972ba41cfa031fcc85da529c1e0183d4459be059d43899182b55c6b5e1e')
    version('1.18.0', sha256='cbb55dfb33df0076a6869ea6f26b9d84c8a579457e25b477a4a9097c035852db')
    version('1.17.0', sha256='0806b1c1445bf9bc418d91bb949cd005009213a88a2145311349d2250230b515')

    version('1.11.0', sha256='b764f8ed16707493003b66845a90c9c79d49bb3d6b2d57f38760fbf324ab6308')
   
    variant('sim',default=False,description='Enable sim version of AliceO2')

    depends_on('o2-aliceo2+sim',when='+sim')
    depends_on('o2-aliceo2', when='~sim')

    depends_on('o2-control+occ')

    def cmake_args(self):
        args = []
        return args
