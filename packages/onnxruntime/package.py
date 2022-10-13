# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *

class Onnxruntime(CMakePackage):
    """ONNX Runtime: cross-platform, high performance ML inferencing and
    training accelerator"""

    homepage = "https://onnxruntime.ai/index.html"
    git = "https://github.com/microsoft/onnxruntime.git"

    def submodules(package):
        submodules = []
        submodules.append("cmake/external/date")
        submodules.append("cmake/external/onnx")
        submodules.append("cmake/external/eigen")
        submodules.append("cmake/external/nsync")
        submodules.append("cmake/external/SafeInt")
        submodules.append("cmake/external/json")
        submodules.append("cmake/external/pytorch_cpuinfo")
        submodules.append("cmake/external/flatbuffers")
        return submodules

    version('1.12.1', tag='v1.12.1', submodules=submodules)

    depends_on('protobuf ~shared')
    depends_on('python@3.5:')
    depends_on('re2')
    depends_on('boost')
    depends_on('py-pybind11')
    depends_on('py-numpy@1.16.6:')
    depends_on('ninja',type='build')

    root_cmakelists_dir = 'cmake'

    generator = 'Ninja'

        
    def cmake_args(self):
        args = []
        args.append(self.define("onnxruntime_BUILD_SHARED_LIB",True))
        args.append(self.define("onnxruntime_BUILD_UNIT_TESTS",False))
        args.append(self.define("onnxruntime_DEV_MODE",False))
        args.append(self.define("onnxruntime_ENABLE_PYTHON",True))
        args.append(self.define("onnxruntime_PREFER_SYSTEM_LIB",True))
        args.append(self.define("onnxruntime_USE_PREINSTALLED_NSYNC",True))
        args.append(self.define("protobuf_USE_STATIC_LIBS",True))
        #args.append(self.define("FLATBUFFERS_INCLUDE_DIR","{}/include".format(self.spec["flatbuffers"].prefix)))
        return args
