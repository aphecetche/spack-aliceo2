# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Asiofi(CMakePackage):
    """C++ Boost.Asio language bindings for OFI libfabric."""

    # FIXME: Add a proper url for your package's homepage here.
    url      = "https://github.com/FairRootGroup/asiofi/archive/v0.3.3.tar.gz"
    homepage      = "https://github.com/FairRootGroup/asiofi"
    git      = "https://github.com/FairRootGroup/asiofi.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.4.3', sha256='d2fc677f30b475d602db4c4e4cdfb54408c44fdcac1095e20c63ac5553cb884c')
    version('0.4.2', sha256='47c2ceb29df22846f635cd0bd13b7652c01a3a826bc0734945369b9e3218345e')
    version('0.4.1', sha256='56271c8943821e8d15320afb773baed062983fe7a7d977c430465de7e6990861')
    version('0.4.0', sha256='fab3aa5a1ef3a0fb8f7852e04658f8957a9c68bdb3ee4b425d43480fa91c316e')
    version('0.3.3', sha256='6e41b1e0502b9758479ef104e060c23c20b36c6f64af356b291a75b7ad6118c6')
    version('0.3.2', sha256='411255477322d1cc8b403abc4f9606c40dd880ba181839227837cda5ce9cc88d')
    version('0.3.1',
            sha256='c18217634cf51c157ff3a21948245a9820eba3eb9d41d875ed6521dd85745fce',preferred=True)
    version('0.3.0', sha256='7322730a6b69414715997e9bac8630bebf42381705ea5418b53fe807b9e4898b')
    version('0.2.1', sha256='2289ad44ef4669420967e9d8cf9e7667e6c19fa4fa5eb651d2710e76a3942a6c')
    version('0.2.0', sha256='2de5efd46d582f37d9863fb7d85106b1951cf54483f50da3eec3a9e22b1a8ec5')

    # FIXME: Add dependencies if required.
    depends_on('boost')
    depends_on('libfabric')

    depends_on('cmake',type='build')
    depends_on('ninja', type='build')

    generator = 'Ninja'

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = [
            "-DDISABLE_COLOR=ON",
            "-DBUILD_SHARED_LIBS=ON",
            "-DBUILD_TESTING=ON",
            "-DOFI_ROOT=" + self.spec['libfabric'].prefix ]
        return args
