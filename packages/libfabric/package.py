# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Libfabric(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    url      = "https://github.com/ofiwg/libfabric/archive/v1.7.1.tar.gz"
    homepage      = "https://github.com/ofiwg/libfabric"
    git      = "https://github.com/ofiwg/libfabric.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.10.1',    sha256='159dc44084afa89278ca2c471120635adb8fbdd4aa3bb61e4249c8e6ba6a83e6')
    version('1.10.0rc3', sha256='f4599ab07276792931d3ce59edac70326360c01a056f4247013faa0ab4e3f278')
    version('1.10.0rc2', sha256='8267448e1fce375f4e23844fc5f0723be9317ce9f3095c38a150bbf359e7bd89')
    version('1.10.0rc1', sha256='300db38d4a2a1201cee3c515ff157151bb5ebdec4c94730ec412822b873f394a')
    version('1.10.0',    sha256='1c157175b5630f16c96bae81e4ec693d7f04ff96f050301ff0b640ed3b91c255')
    version('1.9.1rc2',  sha256='7faf532ff28d4cbf9c4469b7a9e4291507f353c98894b87f323dfd53a117d295')
    version('1.9.1rc1',  sha256='ad0ac32158237f6754f1aca6f89fd3146d99a754448d9cc6ae524883731d2cbe')
    version('1.9.1',     sha256='765fdf71d99d179d89480c82271f62da5f186f61fe3907b1a450a63713312c6a')
    version('1.9.0rc3',  sha256='54c571e22c4d04e84aa7ab5d94dff6514f6d1e2334d633b89318dc42aba32de3')
    version('1.9.0',     sha256='b27537026a8982ea7f1941c9792409386a9b3b6ef539bd7e52fa90e1addbbb4a')
    version('1.7.1',
            sha256='5482eed23d160023f64cbe2322d8329be89f391458d86360cdb6db026f09a912',
            preferred=True)

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    # FIXME: Add additional dependencies if required.
    # depends_on('foo')

    def autoreconf(self, spec, prefix):
        # FIXME: Modify the autoreconf method as necessary
        autoreconf('--install', '--verbose', '--force')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
