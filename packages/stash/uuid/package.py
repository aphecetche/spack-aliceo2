# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Uuid(AutotoolsPackage):
    """Mirror of UUID as used by ALICE experiment"""

    homepage = "https://github.com/alisw/uuid"
    url      = "https://github.com/alisw/uuid/archive/v2.27.1.tar.gz"

    version('2.27.1', sha256='1d61b760835118bc8b5ca24e9ff32206ef266f0ebaaf3c412c11a702b94d4b83')
    version('1.6.2',  sha256='aad32bee7b912b5447d05d53cb5d26540880f3b2113d7acaccb2e3b2daf83cf7')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('python@2.7:')
    depends_on('pkgconfig')

    build_targets = [ 'libuuid.la' ]
    install_targets = [ 'install-uuidincHEADERS' ]

    def autoreconf(self, spec, prefix):
        # FIXME: Modify the autoreconf method as necessary
        autoreconf('--install', '--verbose', '--force')

    def configure_args(self):
        args = []
        args.append('--disable-all-programs')
        args.append('--disable-silent-rules')
        args.append('--disable-tls')
        #args.append('--disable-rpath')
        args.append('--without-ncurses')
        args.append('--enable-libuuid')
        args.append('--disable-use-tty-group')
        args.append('--disable-makeinstall-chown')
 
        if self.spec.satisfies('platform=darwin'):
          args.append('--enable-shared=no')
        return args
