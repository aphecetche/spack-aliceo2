# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
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
#     spack install aliceo2
#
# You can edit this file again by typing:
#
#     spack edit aliceo2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class O2Aliceo2(CMakePackage):
    """ O2 software project for the ALICE experiment at CERN
    """

    homepage = "https://aliceo2group.github.io"
    url = "https://github.com/AliceO2Group/AliceO2/archive/v20.49.tar.gz"

    version(
        '20.49', sha256='f7bda483c4f6666aa6391af470d0bc15c74d4e6aa3632f8e1492496f80ea569f')

    variant('sim', default=False,
            description='Enable simulation engines and event generators')

    depends_on('protobuf')
    depends_on('o2-infologger')
    depends_on('o2-configuration')
    depends_on('o2-monitoring')
    depends_on('o2-common')
    depends_on('rapidjson')
    depends_on('fairroot', when='+sim')
    depends_on('fairroot~sim', when='~sim')
    depends_on('root+http+dataframe')
    depends_on('vmc')
    depends_on('libuv')
    depends_on('vc')
    depends_on('arrow')
    depends_on('ms_gsl@:2.1')
    depends_on('benchmark')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("BUILD_SIMULATION", "sim"))
        return args

    def patch(self):
        filter_file(r'find_package\(fmt\)',
                    '\n\n'+r'find_package(VMC)' + '\n\n'
                    r'find_package(fmt)',
                    'dependencies/O2Dependencies.cmake')
        filter_file(r'ROOT::ROOTDataFrame', r'ROOT::ROOTDataFrame ROOT::VMC',
                    'dependencies/FindFairRoot.cmake')
