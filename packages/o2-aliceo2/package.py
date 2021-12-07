# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import inspect
import multiprocessing
import sys
import platform
import os

class O2Aliceo2(CMakePackage):
    """ O2 software project for the ALICE experiment at CERN
    """

    homepage = "https://aliceo2group.github.io"
    url="https://github.com/AliceO2Group/AliceO2/archive/refs/tags/nightly-20210512.tar.gz"
    git = "https://github.com/AliceO2Group/AliceO2.git"

    version('dev', branch='dev')

    # wrong usage of typeof in EventVizualisation version('20211206', sha256='9d1f7fda7389ed6933dda72a08ab58cfe0a18469663b4182ccd30973d04310da')

    version('20211204', sha256='33fc6e4893e326a878a6de46d919073c04cdc64def90c45153c9a2d2abef0030')

    version('20211024', sha256='e0c5bcd4afce8ff0933ad5117459bd93a89b9000ffdbdc3c53e04e5ca5e1fede')
    version('20211020', sha256='f17aca217a7cd0c66df5b0ecc668e9d1be6b17f59141106c26b38a0a339f2770')
    version('20211019', sha256='9005405c1f18efde46567e581172e0b3a957f9d5a09025824dbfce17714d228b')
    version('20211018', sha256='a6c0533b47ff63c8dd7ce1c2512bab29ec8fe4c0da83f3faba1259adbea382ff')
    version('20211017', sha256='a56044dd5afe7ac46f30cf909549e43b5bf63bf7363a619ef5fabc88408377e2')
    version('20211015', sha256='07e55f34f6b435b081345d48321fa02df89dd7ae0d6efb4107d5e4f88cfb7b61')
    version('20211012', sha256='b8e3c149b27f8a98cf780f2403817b3ef0d0becc8a9419ab87a7434bdc257a0b')
    version('20210913', sha256='93a6b9a2b934d239c7fa326913ef56e7a12d633f4ed52cac07c3991aec3c5a7a')
    version('20210912', sha256='07d0c6b9c3997b0a173e5d3f6aace1611e4248227feee76b102015a7b7599ce5')
    version('20210901', sha256='ac1626dd85d7c0f12fba2aa93eb571da1af68c8aae6e3e5782896ba92ee6317f')
    version('20210818', sha256='c2fd2fb27185a8aed107d262280d63b5f28e99d26ecc5814a4300ee928848e62')
    version('20210516', sha256='5d5626647666969df74573e6ba6f3f7f4a904c081332e3218a2670b7d1ad5733')

    variant('sim', default=False, description='Enable simulation engines and event generators')
    variant('analysis', default=False, description='Enable analysis code')
    variant('cxxstd',default='17',values=('17','20'),multi=False,description="Force a specific C++ standard")
    variant('upgrades',default=False,description='Include code for detector upgrades')
    variant('tsan',default=False,description='Build with ThreadSanitizer')
    variant('asan',default=False,description='Build with AddressSanitizer')
    variant('usan',default=False,description='Build with UndefinedBehaviorSanitizer')

    depends_on('arrow~brotli+compute+gandiva~glog~hdfs+ipc~jemalloc+lz4~parquet~python+shared~snappy+tensorflow+zlib~zstd cxxstd=17')
    depends_on('benchmark')

    depends_on('cppgsl@3: cxxstd=17',when='cxxstd=17')

    depends_on('fairroot', when='+sim')
    depends_on('fairroot~sim', when='~sim')
    depends_on('libuv')
    depends_on('o2-common')
    depends_on('o2-configuration')
    depends_on('o2-infologger')
    depends_on('o2-monitoring')
    depends_on('protobuf')
    depends_on('pythia6',when='+sim')
    depends_on('pythia8',when='+sim')
    depends_on('hepmc3',when='+sim')
    depends_on('rapidjson')
    depends_on('root+xrootd+http+dataframe+arrow~vmc', when='~sim')
    depends_on('root+xrootd+http+dataframe+arrow+pythia6+pythia8~vmc', when='+sim')
    depends_on('vc')
    depends_on('vmc')
    depends_on('libjalieno2')
    depends_on('fftw precision=float ~mpi')
    depends_on('o2-debuggui')
    depends_on('jalien-root')
    depends_on('o2-mcsteplogger',when='+sim')
    depends_on('fastjet',when='+analysis')
    depends_on('fjcontrib',when='+analysis')

    depends_on('ninja', type='build')
    generator = 'Ninja'

    # if sys.platform == 'darwin' and platform.machine() == 'arm64':
    #     patch('no_cpuid_on_apple_silicon.patch')

    #patch('analysis-changes.patch',when='+analysis')
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
        args.append(self.define("CMAKE_EXPORT_COMPILE_COMMANDS",True))
        if sys.platform == 'darwin':
            args.append(self.define("CMAKE_CXX_EXTENSIONS",False))
        if self.spec.satisfies('+asan'):
            args.append(self.define("CMAKE_C_FLAGS","-g -fno-omit-frame-pointer -fsanitize=address"))
            args.append(self.define("CMAKE_CXX_FLAGS","-g -fno-omit-frame-pointer -fsanitize=address"))
            args.append(self.define("CMAKE_EXE_LINKER_FLAGS","-fsanitize=address"))
            args.append(self.define("CMAKE_SHARED_LINKER_FLAGS","-fsanitize=address"))
            args.append(self.define("CMAKE_MODULE_LINKER_FLAGS","-fsanitize=address"))
        if self.spec.satisfies('+tsan'):
            args.append(self.define("CMAKE_CXX_FLAGS","-fsanitize=thread"))
        if self.spec.satisfies('+usan'):
            args.append(self.define("CMAKE_C_FLAGS","-g -fno-omit-frame-pointer -fsanitize=undefined"))
            args.append(self.define("CMAKE_CXX_FLAGS","-g -fno-omit-frame-pointer -fsanitize=undefined"))
            args.append(self.define("CMAKE_EXE_LINKER_FLAGS","-fsanitize=undefined"))
            args.append(self.define("CMAKE_SHARED_LINKER_FLAGS","-fsanitize=undefined"))
            args.append(self.define("CMAKE_MODULE_LINKER_FLAGS","-fsanitize=undefined"))
        return args
  
    def setup_root_include_path(self,env):
        # this is needed e.g. to compile Root macros for the tests
        for d in self.spec.traverse():
            #print(d.name,d.prefix.include)
            env.append_path("ROOT_INCLUDE_PATH",d.prefix.include)
        env.append_path("ROOT_INCLUDE_PATH",self.prefix.include)

    def setup_build_environment(self,env):
        # FIXME: this should not be necessary with Spack, but 
        # in AliceO2/cmake/dependencies we explicitely ask for PYTHIA[#]_ROOT
        # to be env. variables for aliBuild...
        if self.spec.satisfies('+sim'):
          env.set('PYTHIA6_ROOT',self.spec['pythia6'].prefix)
          env.set('PYTHIA_ROOT',self.spec['pythia8'].prefix)
          env.set('HEPMC3_ROOT',self.spec['hepmc3'].prefix)
        self.setup_root_include_path(env)

    def setup_environment(self, spack_env, run_env):
        run_env.set('O2_ROOT',self.prefix)
        run_env.set('VMCWORKDIR',os.path.join(self.prefix,"share"))
        run_env.append_path("ROOT_INCLUDE_PATH",self.prefix.include)
        run_env.append_path("ROOT_INCLUDE_PATH",os.path.join(self.prefix.include,"GPU"))
        # if self.spec.satisfies('+sim'):
        #     run_env.set('HEPMC3_ROOT',self.spec['hepmc3'].prefix)
        self.setup_root_include_path(run_env)


    def patch(self):
        # filter_file(r'find_package\(fmt\)',
        #             '\n\n'+r'find_package(VMC)' + '\n\n'
        #             r'find_package(fmt)',
        #             'dependencies/O2Dependencies.cmake')
        # filter_file(r'ROOT::ROOTDataFrame', r'ROOT::ROOTDataFrame ROOT::VMC',
        #             'dependencies/FindFairRoot.cmake')
        # filter_file(r'NAMES libpythia6.so libpythia6.dylib',
        #         'NAMES libpythia6.so libpythia6.dylib libPythia6.so libPythia6.dylib',
        #         'dependencies/Findpythia6.cmake')
        pass
