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
#     spack install py-async-stagger
#
# You can edit this file again by typing:
#
#     spack edit py-async-stagger
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyAsyncStagger(PythonPackage):
    """Happy Eyeballs connection algorithm and underlying scheduling logic in asyncio"""

    url      = "https://files.pythonhosted.org/packages/d3/8a/e38a29f65f1a28ad0a19f9dfdb084a0fae4ca1be630aa3c34511d219e54c/async_stagger-0.3.0.tar.gz"


    version('0.3.0', sha256='1c7817ccb2e85d8179742417b5e7ecbf9e114345e9e3bac7feae89b91c29f400')

    depends_on('py-setuptools', type='build')

    def build_args(self, spec, prefix):
        args = []
        return args
