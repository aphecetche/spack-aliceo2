# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class O2Pdpsuite(BundlePackage):
    """AliceO2 PDP Suite."""
  
    homepage=""

    version("latest")

    depends_on('o2-aliceo2 +sim+analysis')
    depends_on('o2-datadistribution')
    depends_on('o2-qualitycontrol')
    depends_on('o2-dpg')

