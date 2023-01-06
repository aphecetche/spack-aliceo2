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
#     spack install fftw
#
# You can edit this file again by typing:
#
#     spack edit fftw
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import platform

class Fftw(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "http://fftw.org/fftw-3.3.9.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('3.3.10', sha256='56c932549852cddcfafdab3820b0200c7742675be92179e59e6215b340e26467')
    version('3.3.9', sha256='bf2c7ce40b04ae811af714deb512510cc2c17b9ab9d6ddcf49fe4487eea7af3d')

    variant(
      'precision', values=any_combination_of(
          'float', 'double', 'long_double', 'quad'
       ).prohibit_empty_set().with_default('float,double'),
       description='Build the selected floating-point precision libraries'
    )
    variant('openmp', default=False, description="Enable OpenMP support.")
    variant('mpi', default=False, description='Activate MPI support')

    depends_on('mpi', when='+mpi')
    #depends_on('llvm-openmp', when='%apple-clang +openmp')%%

    provides('fftw-api@3', when='@3:')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        args.append(self.define("ENABLE_FLOAT",'precision=float' in self.spec))
        args.append(self.define("ENABLE_LONG_DOUBLE",'precision=long_double' in self.spec))
        args.append(self.define("ENABLE_QUAD_PRECISION",'precision=quad' in self.spec))
        args.append(self.define("ENABLE_AVX",platform.machine()!='arm64'))
        return args
