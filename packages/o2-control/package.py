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

    version('0.20.3', sha256='4dc36bff618e9aec24d3dd6ee2b1f8db75713c144c349a9c5abd48542d956af4')

    variant('core',default=True,description='build control core')
    variant('occ',default=True,description='build control occ plugin')
    variant('coconut',default=False,description='build coconut')

    depends_on('fairmq',when='+occ')
    depends_on('fairlogger',when='+occ')
    depends_on('boost',when='+occ')
    depends_on('protobuf',when='+occ')
    depends_on('openssl',when='+occ')
    depends_on('o2-infologger+libonly',when='+occ')
    depends_on('o2-configuration',when='+occ')
    depends_on('fmt',when='+occ')
    depends_on('abseil-cpp',when='+occ')
    depends_on('grpc@1.34: +shared',when='+occ')
    depends_on('rapidjson',when='+occ')

    depends_on('cmake', type='build', when='+occ')
    depends_on('ninja', type='build', when='+occ')

    def install(self,spec,prefix):
       if self.spec.satisfies('+occ'):
           self.build_occ()

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
