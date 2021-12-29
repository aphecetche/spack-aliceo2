# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class O2Mcsteplogger(CMakePackage):
    """A facility to monitor step data of Virtual Monte Carlo simulation non-invasively."""

    homepage = "https://github.com/AliceO2Group/VMCStepLogger"
    git = "https://github.com/AliceO2Group/VMCStepLogger.git"
    url = "https://github.com/AliceO2Group/VMCStepLogger/archive/refs/tags/v0.2.0.tar.gz"

    version('master', branch='master')
    version('0.4.0', sha256='45ee718de82ceee873becf69e4827c9b29a1be2874cbcfc0f34768f7761be853')

    depends_on('boost')
    depends_on('root')
    depends_on('vmc')

    def cmake_args(self):
        args = ["-DBUILD_SHARED_LIBS=ON",
                "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON"]
        return args
