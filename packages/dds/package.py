# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
#   Spack Project Developers. See the top-level COPYRIGHT file for details.
# Copyright 2019-2020 GSI Helmholtz Centre for Heavy Ion Research GmbH,
#   Darmstadt, Germany
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import inspect
import multiprocessing

class Dds(CMakePackage):
    """The Dynamic Deployment System (DDS)
       A tool-set that automates and significantly simplifies a deployment
       of user defined processes and their dependencies on any resource
       management system using a given topology.
    """

    homepage = "http://dds.gsi.de"
    git = "https://github.com/FairRootGroup/DDS"
    url = "https://github.com/FairRootGroup/DDS/archive/3.5.4.tar.gz"
    maintainers = ['dennisklein', 'ChristianTackeGSI']

    version('develop', branch='master', get_full_repo=True)

    version('3.5.17', sha256='35723797e0cc39177946655192fa861c2fcae91deae82a5acd6e2ce1b67bc974')
    version('3.5.16', sha256='8f4922d95f93f7e731c239be990c4515299eccb9d067678012b8553b37c2d318')
    version('3.5.12', sha256='2f76e70d4f689020030b3ea780916d01acb1cc31e0e34edd4c168046d9491ff3')
    version('3.5.11', sha256='c478f3907a74681fd4cb51887a03f3497010e286531563943706d557ed472ec1')
    version('3.5.10', sha256='ac899977d2705e2a0c5cfc1b0ec46387bf96d561d92e9e08509dda093edb264a',preferred=True)
    version('3.5.9', sha256='632dd966e63e0ec8ff584bd3fb23584495f46c0afabe0fb03d455946b6cfeb66')
    version('3.5.8', sha256='461c8932993fb8c671a8e3bc32190c1ce40e407e1fa4f2c3894f0ec1cf62f2da')
    version('3.5.7', sha256='03998b67b732535265746800ca69f798d6c0d5d4f86eedd8c30896a62e5be5b5')
    version('3.5.6', sha256='b99160f7862646162d922c0c37c4a64d6bfccad3f99b55fbbd3a76252592117f')
    version('3.5.5', sha256='fb47e42466926e195cc5a795fc6043a44aa337e416aaa0bdf0d9cfb099d25e9b')
    version('3.5.4', sha256='901fc9cb5197c01a3824bb5cc6c9ad21cb2f93e764d99d7948d65b63670cf635')
    version('3.5.3', commit='f1eae89fdff266be86ec962c19e1c7930baf002c', no_cache=True)
    version('3.5.2', tag='3.5.2', commit='0813fd5772d1836c055370f4f16d46c961aa0d19', no_cache=True)
    version('3.4', tag='3.4', commit='e0900e946069d840c76e00f29113fd56158fdaa4', no_cache=True)
    version('3.2', tag='3.2', commit='03efdc71eb9aa35091ed1fbc41680c44e2ac7f54', no_cache=True)
    version('3.0', tag='3.0', commit='8b00716622962929ab4e19d0bb13e761d955fd87', no_cache=True)
    version('2.5-odc', tag='2.5-odc', commit='77d8452e15b390eaa6314c78c6073c3a9d687202', no_cache=True)
    version('2.4', tag='2.4', commit='7499753bdec9b5ed2468a712e57c5578ca25e7a6', no_cache=True)
    version('2.2', tag='2.2', commit='7c633d61d011af6e38c591152d77a979f841ce8c', no_cache=True)
    # TODO Once https://github.com/spack/spack/issues/14344 is resolved, enable
    #      source caching again (by removing the `no_cache` argument).

    patch('fix_wn_bin_2.2.patch', when='@2.2')
    patch('fix_wn_bin_2.4.patch', when='@2.4')
    patch('fix_wn_bin_2.5-odc.patch', when='@2.5-odc')
    patch('fix_wn_bin_3.0.patch', when='@3.0')
    patch('fix_wn_bin_3.2_3.5.2.patch', when='@3.2:3.5.2')
    patch('fix_wn_bin_3.5.3.patch', when='@3.5.3')
    patch('fix_wn_bin_master.patch', when='@develop')
    patch('fix_wn_bin_3.5.4_3.5.10.patch', when='@3.5.4:3.5.10')
    patch('fix_wn_bin_3.5.14.patch', when='@3.5.14')
    patch('fix_wn_bin_3.5.16.patch', when='@3.5.16')
    # TODO Upstream the wn_bin fix
    patch('fix_uuid_init.patch', when='@2.5-odc:3.0')

    depends_on('boost@1.67:1.72 +shared+log+thread+program_options+filesystem+system+regex+test',when='@2.4:3.4')
    depends_on('boost@1.74: +shared+atomic+log+thread+program_options+filesystem+system+regex+test',when='@3.5:')
    # TODO No support for Boost 1.73, check if later releases will work
    # https://github.com/FairRootGroup/DDS/commit/e5b8ca86c46220238d130ac1f3f15dff32e85a2a
    # https://github.com/FairRootGroup/DDS/issues/305
    depends_on('boost@1.67:1.68 +shared+log+thread+program_options+filesystem+system+regex+test+signals', when='@:2.3')
    conflicts('^boost@1.70:', when='^cmake@:3.14')

    depends_on('cmake@3.16:', type='build')
    depends_on('git', type='build')

    variant('cxxstd', default='default',
            values=('11', '14', '17'),
            multi=False,
            description='Force the specified C++ standard when building.')

    build_targets = ['all', 'wn_bin']

    def build(self, spec, prefix):
      inspect.getmodule(self).make.jobs=multiprocessing.cpu_count()*2//5
      super().build(spec,prefix)

    @run_before('cmake')
    def create_version(self):
        with open('version','w') as f:
            f.write('{}'.format(self.version))

    def cmake_args(self):
        args = []
        #args.append(self.define('Boost_NO_SYSTEM_PATHS',True))
        #args.append(self.define('BOOST_ROOT',self.spec['boost'].prefix))
        if self.spec.satisfies('@:2.5'):
            args.append('-DBUILD_SHARED_LIBS=ON')
        cxxstd = self.spec.variants['cxxstd'].value
        if cxxstd != 'default':
            args.append('-DCMAKE_CXX_STANDARD=%s' % cxxstd)
        if self.spec.satisfies('^boost@:1.69.99'):
            args.append('-DBoost_NO_BOOST_CMAKE=ON')
        return args
