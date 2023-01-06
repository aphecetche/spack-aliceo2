# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class O2Infologger(CMakePackage):
    """AliceO2 logging library"""

    homepage = "https://github.com/AliceO2Group/InfoLogger"
    url = "https://github.com/AliceO2Group/InfoLogger/archive/v1.3.9.tar.gz"
    git = "https://github.com/AliceO2Group/InfoLogger.git"

    variant('libonly', default=True, description='Builds only the library')

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('master', branch='master')

    version("2.5.3", sha256="a5e76424857924afdf79e761bd59a880c75758dc04a12160e52bf6f61922b5d8")
    version("2.5.2", sha256="ac05ed8951e410b3a19f3458fa8240fd2a09906f63e9dd71113e6d2cc7389d0d")
    version('2.5.1', sha256='c942d183b58b8ee31ca2b3dd03f43ec415bd5105986f6909bf07d7b1683fce50')
    version('2.5.0', sha256='0d1225d23b655c7decb011a5abf6f218077baa48cc5549ef01735b5dc53b52d6')
    version('2.4.3', sha256='7ef7f01e3e2dba41413556135dd5c4e4d7bf6a031bc5b54b739bbade0fc4f526')
    version('2.4.1', sha256='416431ef6bd6996ca14b97733f54061ba45ba4de35b468e0c30c47243d56b183')
    version('2.4.0', sha256='01caaad596622cbe32fd4ebfadb0d93857bce379850c31ec2b7d03534e0a41d7')
    version('2.2.0', sha256='04eea3ca40e562bddd1b442a999acd3487d0749e2200a967a7d7a98f2c64ad5e')
    version('2.1.1', sha256='418c2d582117f9d9dc7a2d5c5b4b1c3190542bd565954b1bbba434cd6649f764')
    version('2.1.0', sha256='709a19aa25e5557d91c37abdf721d5b559bf550304925e9620878f6f9143e497')

    version('2.0.1', sha256='e2fc85d80b3ee3189e962da02c872eff68c944c989d0820d3c4059b084574c5a')
    version('1.3.16', sha256='b9949769678e8a1ff9a84630432fff53400c9910b5415a05e4c61fb0bada62de')
    version('1.3.9', '350dbe5bd8d0a121e53828b79341487b')

    depends_on('boost +container cxxstd=17')
    depends_on('mariadb-client', when='-libonly')
    depends_on('swig', when='-libonly', type='build')
    depends_on('go', when='-libonly', type='build')
    depends_on('cmake', type='build')
    depends_on('ninja', type='build')

    generator = 'Ninja'

    def cmake_args(self):
        args = ['-DINFOLOGGER_BUILD_LIBONLY=%d' %
                (1 if '+libonly' in self.spec else 0)]
        return args
