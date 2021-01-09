# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class AlienCas(Package):
    """AliEn Certification Authority certificates."""

    homepage      = "https://github.com/alisw/alien-cas"
    git      = "https://github.com/alisw/alien-cas.git"

    version('1',commit='53fbc54de2fc99129eff587ac0dd6dc814b0439e')

    def install(self, spec, prefix):
        dest = '{}/globus/share/certificates'.format(prefix)
        mkdirp(dest)
        install_tree('.',dest)
