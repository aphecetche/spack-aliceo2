# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class O2Control(Package):
    """AliECS - The ALICE Experiment Control System"""

    homepage = "https://github.com/AliceO2Group/Control"
    url = "https://github.com/AliceO2Group/Control/archive/v0.20.3.tar.gz"
    git = "https://github.com/AliceO2Group/Control.git"

    version('0.50.0', sha256='75fa2dd4cc35639dfe0d421a65025bf8eef630b03c289532f08c0dafa6ef9ae4')
    version('0.49.0', sha256='f534f408936a794266d5b395276d3419b0de9f2d1c771ae2d989de5acda1dc22')

    version('0.38.80', sha256='ed6d007dadefdac722b62e284b91501215c5050b4f4d9157693f731ac2daa9a6')
    version('0.30.1', sha256='3cd776c5b66b993dd24b3c4160d88257eff2374d10bd6ae15533ff2771da02c8')
    version('0.29.0', sha256='f725824889e2f17a6e443da5ab497d1e27702f0df8cccba167d675f158fb18c4')
    version('0.27.80', sha256='2fe09d10023948dc1cf43f695647976849f6db82111de0f8d7282d481aaae688')
    version('0.27.0', sha256='c9bff4fcbb555d615fd53ce5bc61a8b8c943f527bf45a69874277e408de39188')
    version('0.26.5', sha256='b2ae74b6927a0fd4cd59c5075b3cc3fdbb59751a69a1b54511c1f3266cb6cde5')
    version('0.26.4', sha256='80b64f81a078268da45a43d326939fe10eafc153fb1121017666dad438cbdc8a')
    version('0.26.3', sha256='5596ee08b43527a93dc7eef58b80ac6b7938e4d5f6a8834201497bb5c13588ae')
    version('0.26.2', sha256='1b11ccdad0a8978fb3ca4d2e3853549cefd6651e6c9fb95f78afa618abbf6931')

    version('0.23.1', sha256='d3af6914723268a3067b182532e3ec6dff225fe043f160a4e48e9a1848d51a9a')
    #version('0.20.3', sha256='4dc36bff618e9aec24d3dd6ee2b1f8db75713c144c349a9c5abd48542d956af4')

    variant('core',default=True,description='build control core')
    variant('occ',default=True,description='build control occ plugin')
    variant('coconut',default=False,description='build coconut')

    depends_on('fairmq',when='+occ')
    depends_on('fairlogger',when='+occ')
    depends_on('boost',when='+occ')
    depends_on('protobuf@3.14.3:',when='+occ')
    depends_on('openssl',when='+occ')
    depends_on('o2-infologger+libonly',when='+occ')
    depends_on('o2-configuration',when='+occ')
    depends_on('fmt',when='+occ')
    depends_on('abseil-cpp',when='+occ')
    depends_on('grpc@1.34: +shared',when='+occ')
    depends_on('rapidjson',when='+occ')
    depends_on('go',when='+coconut')

    depends_on('cmake', type='build', when='+occ')
    depends_on('ninja', type='build', when='+occ')

    def install(self,spec,prefix):
       if self.spec.satisfies('+occ'):
           self.build_occ()
       if self.spec.satisfies('+coconut'):
           self.build_coconut()

    def cmake_args(self):
        args = ['-DBUILD_SHARED_LIBS=ON']
        return args

    def build_occ(self):
        args = self.cmake_args()
        args.extend(std_cmake_args)
        with working_dir('occ'):
            with working_dir('spack-build', create=True):
                cmake('..','-DBUILD_SHARED_LIBS=ON',*args)
                make()
                make("install")

    def build_coconut(self):
        make("vendor")
        make("WHAT=coconut")
        make("install")
