# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os
import re
from shutil import copy

class AlienCas(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    git      = "https://github.com/alisw/alien-cas.git"

    version('master', branch='master')

    def setup_environment(self, spack_env, run_env):
        run_env.set('X509_CERT_DIR',prefix.share)

    def install(self, spec, prefix):
        os.mkdir(prefix.share)
        path = os.walk('.')
        for root, directories, files in path:
            print("root=",root)
            if re.search('igtf',root) or re.search('alien-ca',root):
                for file in files:
                    copy(os.path.join(root,file),prefix.share)
