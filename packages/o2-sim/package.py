# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class O2Sim(BundlePackage):
    """Meta package for AliceO2 sim related stuff."""

    homepage = ""

    version('latest')

    depends_on('o2-physics')
    depends_on('o2-dpg')
    depends_on('o2-aegis')
    depends_on('o2-evtgen')
