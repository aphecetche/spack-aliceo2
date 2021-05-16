# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import inspect
import multiprocessing
import sys
import platform

class O2Aliceo2(CMakePackage):
    """ O2 software project for the ALICE experiment at CERN
    """

    homepage = "https://aliceo2group.github.io"
    url="https://github.com/AliceO2Group/AliceO2/archive/refs/tags/nightly-20210512.tar.gz"
    git = "https://github.com/AliceO2Group/AliceO2.git"

    version('dev', branch='dev')
    version('20210512', sha256='5d5626647666969df74573e6ba6f3f7f4a904c081332e3218a2670b7d1ad5733')
    version('21.09',sha256='588f9c9a934f5fa29373c64a5e6b9617299bc58f6940e570ad032c78b1b972c9')
    version('21.05',sha256='d54fc6db40c71a9b8f01466509638127df945cb2806e31699a9d25deb39382d7')
    version('21.03',sha256='7f7060e3140f14a30fe54985ad22dfd322d7abb876e6fff526a1969823f18736')

    variant('sim', default=False, description='Enable simulation engines and event generators')
    variant('analysis', default=False, description='Enable analysis code')
    variant('cxxstd',default='17',values=('17','20'),multi=False,description="Force a specific C++ standard")
    variant('upgrades',default=False,description='Include code for detector upgrades')

    depends_on('arrow~brotli+compute+gandiva~glog~hdfs+ipc~jemalloc+lz4~parquet~python+shared~snappy+tensorflow+zlib~zstd cxxstd=17')
    depends_on('benchmark')

    if sys.platform == 'darwin' and platform.machine() == 'arm64':
       depends_on('cppgsl@3: cxxstd=17',when='cxxstd=17')
    else:
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
    depends_on('hepmc3',when='+sim')
    depends_on('rapidjson')
    depends_on('root+http+dataframe+arrow', when='~sim')
    depends_on('root+http+dataframe+arrow+pythia6+pythia8', when='+sim')
    depends_on('vc')
    depends_on('vmc')

    depends_on('ninja', type='build')
    generator = 'Ninja'

    if sys.platform == 'darwin' and platform.machine() == 'arm64':
        patch('no_cpuid_on_apple_silicon.patch')

    patch('gsl-3-does-not-have-at-method.patch',when='@:21.08 ^cppgsl@3:')
    patch('gsl-3-tpc-changes.patch',when='@:21.08 ^cppgsl@3:')
    patch('gsl-3-mid-changes.patch',when='@:21.08 ^cppgsl@3:')
    patch('gsl-3-ft0-changes.patch',when='@:21.08 ^cppgsl@3:')
    patch('gsl-3-eve-changes.patch',when='@:21.08 ^cppgsl@3:')
    patch('gsl-3-trd-changes.patch',when='@:21.08 ^cppgsl@3:')
    patch('analysis-changes.patch',when='+analysis')
    patch('phos-base-geometry.patch',when='@21.05')

#    def build(self, spec, prefix):
#        inspect.getmodule(self).make.jobs=multiprocessing.cpu_count()*2//5
#        super().build(spec,prefix)

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("BUILD_SIMULATION", "sim"))
        args.append(self.define_from_variant("BUILD_ANALYSIS", "analysis"))
        args.append(self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"))
        args.append(self.define_from_variant("ENABLE_UPGRADES", "upgrades"))
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
        filter_file(r'NAMES libpythia6.so libpythia6.dylib',
                'NAMES libpythia6.so libpythia6.dylib libPythia6.so libPythia6.dylib',
                'dependencies/Findpythia6.cmake')
            
        if self.spec["cppgsl"].satisfies('@3:'):
            filter_file('::index_type','::size_type','Framework/Core/include/Framework/TMessageSerializer.h')
            filter_file('::index_type','::size_type','DataFormats/simulation/include/SimulationDataFormat/ConstMCTruthContainer.h')
            filter_file('::index_type','::size_type','Detectors/GlobalTracking/include/GlobalTracking/MatchTOF.h')
            filter_file('::index_type','::size_type','Utilities/O2Device/include/O2Device/Utilities.h')
