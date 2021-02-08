# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
import inspect
import multiprocessing
import sys
import platform

class MrrtfAlo(CMakePackage):
    """ A small package for Alice Muon Reconstruction development."""

    homepage = "https://github.com/mrrtf/alo"
    url = "https://github.com/mrrtf/alo/archive/v0.5.tar.gz"

    version('0.5',sha256='e69a9ad164c547e221c777f5b88240a0d9c4f32effa4ff90a786d160aadb4198',url='https://github.com/mrrtf/alo/archive/v0.5.tar.gz')

    variant('o2', default=True, description='Enable O2 part')
    variant('cxxstd',default='17',values=('17','20'),multi=False,description="Force a specific C++ standard")

    depends_on('o2-aliceo2+sim',when='+o2')
    depends_on('flatbuffers',when='+o2')

    #variant('aliroot', default=False, description='Enable AliRoot part')
    #depends_on('o2-aliroot',when='+aliroot')

    depends_on('ninja', type='build')
    generator = 'Ninja'

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"))
        #args.append(self.define("Flatbuffers_ROOT",self.spec["flatbuffers"].prefix))
        return args
