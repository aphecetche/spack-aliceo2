# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyWebsockets(PythonPackage):
    """Library for building WebSocket servers and clients in Python https://websockets.readthedocs.io/"""

    # FIXME: Add a proper url for your package's homepage here.
    url      = "https://github.com/aaugustin/websockets/archive/8.1.tar.gz"

    version('8.1',   sha256='c19ce96ad5f7606127d3915364144df93fb865a215784b06048fae3d39364f14')
    version('8.0.2', sha256='9a67f20cf44ea6d8405c37e3b8dae00642f517b94517764e87ebcec768b295fc')
    version('8.0.1', sha256='1039bdbdf25fd341bc10e915f01b7d8a94b0ef394f235df0c11de61f3f25b18f')
    version('8.0',   sha256='686250762aec4f9611357a21334e9932bddbbea890569c4d725675d6e010fde1')
    version('7.0',   sha256='39391d6d8eb1d3973fc104f32df54de653e3d7aa89584a43c761a1b5cb8ed74d')
    version('6.0',   sha256='47bcad3e017925f8688512b4efa760807bf604a939c50c2926c40b0021247cf0')
    version('5.0.1', sha256='e1e1c1213016c6ab71f7a5affd8f3a51bfb87089a72ad8216fe558c5572892c3')
    version('5.0',   sha256='84b7894f17b35efac3aac9efffab3ed81304284c61bef9ea26a170ef684f162e')
    version('4.0.1', sha256='da5068655b1ba5487dbdf36919c54c5721aa148c6388077c18b923b539aafddc')
    version('4.0',   sha256='8742ebb5778098a5b62e995c8e274a03e47d50bae2062a5710feab20e7e18a3c')

    depends_on('py-setuptools', type='build')

    def build_args(self, spec, prefix):
        args = []
        return args
