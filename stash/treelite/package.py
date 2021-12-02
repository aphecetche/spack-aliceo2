# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *

class Treelite(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/dmlc/treelite/archive/refs/tags/0.92.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2.1.0', sha256='9a741e345b7a8c49f4a981fec5fdce71cbcbd7b072f6dd47d0e941c9d52f4a52')
    version('2.0.0', sha256='5e8df3d0c2fc141db82f43c05ce8d5e4353bdba4aa652d58e7b409b4983b5524')
    version('1.3.0', sha256='38babc3be02aa95181f02cc4cb607453ff4c3046dcc7b7aa7795d0a936ae61bf')
    version('1.2.0', sha256='e145ee6e81346494031b5c8008793aa3f1d79e2bf52f54053698072d2eabf6de')
    version('0.93',  sha256='7d347372f7fdc069904afe93e69ed0bf696ba42d271fe2f8bf6835d2ab2f45d5')
    version('0.92',  sha256='17961a4f4c5933630dfee5c7129180e9d69660f3efa05f87bc8b168081bf3fd7')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
