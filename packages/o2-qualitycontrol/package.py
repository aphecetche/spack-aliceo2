# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class O2Qualitycontrol(CMakePackage):
    """Data Quality Control (QC) software for the ALICE O2 system"""

    homepage = "https://github.com/AliceO2Group/QualityControl"
    url="https://github.com/AliceO2Group/QualityControl/archive/refs/tags/v1.28.0.tar.gz"
    git      = "https://github.com/AliceO2Group/QualityControl.git"

    depends_on('ninja', type='build')
    generator = 'Ninja'

    version('master',branch='master')

    version('1.45.1', sha256='55644e0d86d1399ffc4ee73f69d275321a2cc214adc2155af0d40aa56361b4b3')
    version('1.35.1', sha256='5579241ada6f4915eb0270ca9efa374fd2769cdd1190678d11402ae36efdd89e')
    version('1.35.0', sha256='56b704534d90b7cc04bfc92661382cc5469446325daf612079f77312b379e384')
    version('1.34.1', sha256='3de819ce4ece7f9027fc0f6781ffb78b78ef980efe123dc7feeb562c81337dca')
    version('1.34.0', sha256='f7da4253c08d823bc5447f2730ecbf5e0db96c15483554ca3b59ba0637997913')
    version('1.29.1', sha256='fb1bbabec2414f90000be21421dca8feae05f84133298fededbae217502b6681')
    version('1.28.0', sha256='1170972409b1421b3a2520e55caa6222ef8d769323ad3014d566b584035b80c8')

    version('1.24.1', sha256='4b87c3301e3c201807b0e42385bfee722e77130d99eef39d92e1681918c830df')
    version('1.18.1', sha256='4dfb8972ba41cfa031fcc85da529c1e0183d4459be059d43899182b55c6b5e1e')
    version('1.18.0', sha256='cbb55dfb33df0076a6869ea6f26b9d84c8a579457e25b477a4a9097c035852db')
    version('1.17.0', sha256='0806b1c1445bf9bc418d91bb949cd005009213a88a2145311349d2250230b515')

    version('1.11.0', sha256='b764f8ed16707493003b66845a90c9c79d49bb3d6b2d57f38760fbf324ab6308')
   
    variant('sim',default=False,description='Enable sim version of AliceO2')
    variant('tsan',default=False,description='Build with ThreadSanitizer')
    variant('asan',default=False,description='Build with AddressSanitizer')
    variant('usan',default=False,description='Build with UndefinedBehaviorSanitizer')

    depends_on('o2-aliceo2+sim',when='+sim')
    depends_on('o2-aliceo2', when='~sim')

    depends_on('o2-control+occ')

    def cmake_args(self):
        args = []
        args.append(self.define("CMAKE_EXPORT_COMPILE_COMMANDS",True))
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
