# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
#   Spack Project Developers. See the top-level COPYRIGHT file for details.
# Copyright 2020 GSI Helmholtz Centre for Heavy Ion Research GmbH,
#   Darmstadt, Germany
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import sys
import platform

class Fairroot(CMakePackage):
    """C++ simulation, reconstruction and analysis framework for particle physics experiments"""

    homepage = "http://fairroot.gsi.de"
    url = "https://github.com/FairRootGroup/FairRoot/archive/v18.4.0.tar.gz"
    git = "https://github.com/FairRootGroup/FairRoot.git"

    version('develop', branch='dev')

    version("18.4.9", sha256="a62363888fe5535c4c49c4d1603056e4397073f3643aac589db6410b76bd5c5f")
    version('18.6.3',sha256='050132cacd298580dcebe562506e6246eabfcbfd8686d98a5694b38861ee8cd2')
    version('18.6.2',sha256='45762788db5cb705a312fb1b32066677ae8036f588152989554dd8899a42e791')
    version('18.6.1',sha256='8a590b30a3b8dadf6361ea21c073efb9f458f20bf3f25b6937a153068a492998')
    version('18.6.0',sha256='ece7b92c108277e78f8dd4920e5d2a7cec7323ae64b23ffa32874d711dd27a9b')
    version('18.4.8', sha256='3f7df41f0ca2ae62cae925c30eb2a4743f1913d3117fe4bfddbc84a4fd7f5673')
    version('18.4.7',sha256='3e8a7e971f052b1864af607f6bdf72d418870cf0684e02893421ce6a2ea39764')
    version('18.4.5',sha256='483578dccb8722bd7e51133d4025906f8dff8f52d361e67c019fdff99e032279')
    version('18.4.4',sha256='831fcf861710a6c8953a13580ab2f0f855cb0adb2710884be24b2a9edbe42b08')
    version('18.4.3',sha256='243ca688505893e935eb1e1c876e4519c980d409e6602d560c6c983d6366109f')
    version('18.4.2',sha256='abc0ae6e2ba0315a8eecf59cdbf1388dbd1fe6423ab4caaa64f19332252fe05c')
    version('18.4.1',sha256='d8455c4bb705a2d5989ad947ffc50bb2f0d00affb649bb5e30d9463b5be0b490')
    version('18.4.0',sha256='97ad86d039db195acf12e9978eb660daab0c91e95e517921bac5a0f157a3e309')

    version('18.2.1', sha256='a9c22965d2d99e385f64c0df1867b477b9c129bcd087ba3b683d0ada6f3d66d0')

    variant('cxxstd', default='11', values=('11', '14', '17'), multi=False,
            description='Use the specified C++ standard when building.')
    variant('sim', default=True,
            description='Enable simulation engines and event generators')
    variant('examples', default=False,
            description='Install examples')

    generator('ninja')

    depends_on('cmake@3.13.4:', type='build')
    depends_on('boost@1.68.0: +container +filesystem +serialization')
    depends_on('fairlogger@1.4.0:')
    depends_on('fairmq@1.4.11:')
    # depends_on('fairsoft-config', when='@:18,develop')
    depends_on('flatbuffers')
    depends_on('geant3', when="+sim")
    depends_on('geant4', when="+sim")
    depends_on('geant4-vmc', when="+sim")
    depends_on('googletest@1.7.0:')
    depends_on('msgpack-c@3.1:', when='+examples')
    depends_on('protobuf')
    depends_on('pythia6', when='+sim')
    depends_on('pythia8', when='+sim')
    depends_on('root+http',when='~sim')
    depends_on('root+http+pythia6+pythia8',when='+sim')
    depends_on('vgm', when="+sim")
    depends_on('vmc', when='@18.4: ^root@6.18:')
    depends_on('yaml-cpp', when='@18.2:')

    patch('cmake_utf8.patch', when='@18.2.1')
    patch('fairlogger_incdir.patch', level=0, when='@18.2.1')
    patch('find_pythia8_cmake.patch', when='@:18.4.0 +sim')
    patch('support_geant4_with_external_clhep_18.2.patch', when='@18.2 +sim')
    patch('support_geant4_with_external_clhep.patch', when='@18.4 +sim ^Geant4@:10.5')
    patch('darwin_fortran_compiler_detection.patch',when='@18.4.2:')
    if sys.platform=='darwin' and platform.machine() == 'arm64':
        patch('darwin_arm64_do_not_force_compiler.patch',when='@18.4:18.4.8')

    def setup_build_environment(self, env):
        super(Fairroot, self).setup_build_environment(env)
        if self.spec.satisfies('@:18,develop'):
            env.append_flags('CXXFLAGS',
                '-std=c++%s' % self.spec.variants['cxxstd'].value)
        env.unset('SIMPATH')
        env.unset('FAIRSOFT')
        env.unset('FAIRSOFT_ROOT')
        if "platform=darwin" in self.spec:
            env.unset("MACOSX_DEPLOYMENT_TARGET")
            if self.spec.satisfies("%apple-clang@15:"):
                env.append_flags('CXXFLAGS',
                '-D_LIBCPP_ENABLE_CXX17_REMOVED_UNARY_BINARY_FUNCTION')

    def cmake_args(self):
        options = []
        if self.spec.satisfies('@:18,develop'):
            options.append('-DROOTSYS={0}'.format(self.spec['root'].prefix))
            if '+sim' in self.spec:
              options.append('-DPYTHIA8_DIR={0}'.format(self.spec['pythia8'].prefix))

        options.append('-DBUILD_EXAMPLES:BOOL=%s' %
                       ('ON' if '+examples' in self.spec else 'OFF'))

        if self.spec.satisfies('^boost@:1.69.99'):
            options.append('-DBoost_NO_BOOST_CMAKE=ON')

        return options

    def common_env_setup(self, env):
        # So that root finds the shared library / rootmap
        # env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        pass

    def setup_run_environment(self, env):
        self.common_env_setup(env)
        env.prepend_path("ROOT_INCLUDE_PATH",self.prefix.include)

    def setup_dependent_build_environment(self, env, dependent_spec):
        self.common_env_setup(env)

    def setup_dependent_run_environment(self, env, dependent_spec):
        self.common_env_setup(env)

