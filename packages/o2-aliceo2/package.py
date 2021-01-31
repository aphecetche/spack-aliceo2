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
#     spack install aliceo2
#
# You can edit this file again by typing:
#
#     spack edit aliceo2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import inspect
import multiprocessing

class O2Aliceo2(CMakePackage):
    """ O2 software project for the ALICE experiment at CERN
    """

    homepage = "https://aliceo2group.github.io"
    url = "https://github.com/AliceO2Group/AliceO2/archive/v20.49.tar.gz"

    version('noana', '65a2f7da91c8be474a6f09dd457b0cde6b651a85f1709e848eb52c2819652d16',
            url='https://github.com/aphecetche/AliceO2/archive/add-cmake-build-option-to-disable-analysis.tar.gz')

    version('noana-2', '73b768e77e5e9c604e097c5c39c1346275fa15dd3b940cf29778aa17e49284cd',
            url='https://github.com/aphecetche/AliceO2/archive/mods-for-spack.tar.gz')

    version(
        '20.49', sha256='f7bda483c4f6666aa6391af470d0bc15c74d4e6aa3632f8e1492496f80ea569f')

    variant('sim', default=False,
            description='Enable simulation engines and event generators')
    variant('analysis', default=True,
            description='Enable analysis code')
    variant('cxxstd',default='17',values=('17','20'),multi=False,description="Force a specific C++ standard")

    depends_on('arrow~brotli+compute+gandiva~glog~hdfs+ipc~jemalloc+lz4~parquet~python+shared~snappy+tensorflow+zlib~zstd cxxstd=17')
    depends_on('benchmark')
    depends_on('cppgsl@:2.99 cxxstd=17',when='cxxstd=17')
    depends_on('fairroot', when='+sim')
    depends_on('fairroot~sim', when='~sim')
    depends_on('libuv')
    depends_on('o2-common')
    depends_on('o2-configuration')
    depends_on('o2-infologger')
    depends_on('o2-monitoring')
    depends_on('protobuf')
    depends_on('pythia6+root',when='+sim')
    depends_on('pythia8',when='+sim')
    depends_on('rapidjson')
    depends_on('root+http+dataframe+arrow', when='~sim')
    depends_on('root+http+dataframe+arrow+pythia6+pythia8', when='+sim')
    depends_on('vc')
    depends_on('vmc')

    depends_on('ninja', type='build')
    generator = 'Ninja'

#    def build(self, spec, prefix):
#        inspect.getmodule(self).make.jobs=multiprocessing.cpu_count()*2//5
#        super().build(spec,prefix)

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("BUILD_SIMULATION", "sim"))
        args.append(self.define_from_variant("BUILD_ANALYSIS", "analysis"))
        args.append(self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"))
        return args

    def setup_build_environment(self,env):
        # FIXME: this should not be necessary with Spack, but 
        # in AliceO2/cmake/dependencies we explicitely ask for PYTHIA[#]_ROOT
        # to be env. variables for aliBuild...
        if self.spec.satisfies('+sim'):
          env.set('PYTHIA6_ROOT',self.spec['pythia6'].prefix)
          env.set('PYTHIA_ROOT',self.spec['pythia8'].prefix)

    def patch(self):
        filter_file(r'find_package\(fmt\)',
                    '\n\n'+r'find_package(VMC)' + '\n\n'
                    r'find_package(fmt)',
                    'dependencies/O2Dependencies.cmake')
        filter_file(r'ROOT::ROOTDataFrame', r'ROOT::ROOTDataFrame ROOT::VMC',
                    'dependencies/FindFairRoot.cmake')
