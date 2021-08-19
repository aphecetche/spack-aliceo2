# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
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
#     spack install py-onnxruntime
#
# You can edit this file again by typing:
#
#     spack edit py-onnxruntime
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Onnxruntime(CMakePackage):
    """ONNX Runtime: cross-platform, high performance ML inferencing and
    training accelerator"""

    homepage = "https://onnxruntime.ai/index.html"
    url      = "https://github.com/microsoft/onnxruntime/archive/refs/tags/v1.8.2.tar.gz"
    git = "https://github.com/microsoft/onnxruntime.git"

    version('1.8.2', tag='v1.8.2', submodules=True)

    depends_on('protobuf ~shared')
    depends_on('flatbuffers')
    depends_on('python@3.5:')
    depends_on('py-numpy@1.16.6:')
    depends_on('nsync')
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
        return args
