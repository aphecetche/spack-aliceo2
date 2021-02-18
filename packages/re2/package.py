# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Re2(CMakePackage):
    """RE2 is a fast, safe, thread-friendly alternative to backtracking
    regular expression engines like those used in PCRE, Perl, and Python."""

    homepage = "https://github.com/google/re2"
    url = "https://github.com/google/re2/archive/2020-08-01.tar.gz"


    version('2021-02-02', sha256='1396ab50c06c1a8885fb68bf49a5ecfd989163015fd96699a180d6414937f33f')
    version('2021-02-01', sha256='d3e15031ced791b39f11964816ca2d4213f25d3b67fbbe82972c7b7666c456ba')
    version('2020-11-01', sha256='8903cc66c9d34c72e2bc91722288ebc7e3ec37787ecfef44d204b2d6281954d7')
    version('2020-10-01', sha256='0915741f524ad87debb9eb0429fe6016772a1569e21dc6d492039562308fcb0f')

    version('2020-08-01',
            sha256='6f4c8514249cd65b9e85d3e6f4c35595809a63ad71c5d93083e4d1dcdf9e0cd6')
    version('2020-04-01',
            sha256='98794bc5416326817498384a9c43cbb5a406bab8da9f84f83c39ecad43ed5cea')

    version('2019-09-01', sha256='b0382aa7369f373a0148218f2df5a6afd6bfa884ce4da2dfb576b979989e615e')

    variant('shared', default=False, description='Build a shared version of the library')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("BUILD_SHARED_LIBS","shared"))
        # if '+pic' in self.spec:
        #     args.append(self.define('CMAKE_C_FLAGS',
        #                             self.compiler.cc_pic_flag))
        return args
