# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyXjalienfs(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://gitlab.cern.ch/jalien/xjalienfs/-/archive/1.3.3/xjalienfs-1.3.3.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version("1.4.5", sha256="2cf4944a850d5a70d386df4370ba62a67da28125367cb5f2ddff0dbcb5aba339")
    version('1.4.2', sha256='aaeba5d1acf2c3d11806ae657c401e35a2ce5fdcef66af457902e1b7dda765c3')
    version('1.3.3', sha256='1185076ba1c2574b31056eef2bf76508e8532a808a8fc743a81b44e67bf482a7')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    # depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=('build', 'run'))
    depends_on('xrootd +python')
    depends_on('py-websockets')
    depends_on('py-pyopenssl')
    depends_on('py-cryptography')
    depends_on('py-async-stagger')
    depends_on("py-requests")
    depends_on("py-rich")
    depends_on('alien-cas')

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
