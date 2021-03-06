# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class O2Mcsteplogger(CMakePackage):
    """A facility to monitor step data of Virtual Monte Carlo simulation non-invasively."""

    homepage = "https://github.com/AliceO2Group/VMCStepLogger"
    git = "https://github.com/AliceO2Group/VMCStepLogger.git"

    version('master', branch='master')

    depends_on('root+http+xml~x~opengl+vmc')
    depends_on('cmake', type='build')

    def cmake_args(self):
        args = ["-DBUILD_SHARED_LIBS=ON",
                "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON"]
        return args
