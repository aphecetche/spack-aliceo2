# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Fastjet(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/alisw/fastjet/archive/refs/tags/v3.2.1_1.024-alice3.tar.gz"


    version('1.024-alice3', sha256='8b0b2cc4591a42fe00acd77a7fdb2a28bf7895cbe36f7bdd89c2ec168ae544ad')

    depends_on('autoconf',type='build')
    depends_on('automake',type='build')
    depends_on('libtool',type='build')
    depends_on('m4',type='build')

    def configure_args(self):
        return []
