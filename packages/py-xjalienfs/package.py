# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-xjalienfs
#
# You can edit this file again by typing:
#
#     spack edit py-xjalienfs
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyXjalienfs(PythonPackage):
    """Python interface to websocket endpoint of ALICE Grid Services."""

    git = "https://gitlab.cern.ch/jalien/xjalienfs.git"

    version('1.0.7',tag='1.0.7')

    depends_on('py-setuptools', type=('build','run'))

    depends_on('py-python-gnureadline')
    depends_on('py-async-stagger')
    depends_on('py-websockets')
    depends_on('py-pyopenssl')
    depends_on('xrootd@v4.11.1: +python~kerberos',type=('build','run'))

    def build_args(self, spec, prefix):
        args = []
        return args
