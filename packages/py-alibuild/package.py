# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyAlibuild(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/alisw/alibuild/archive/refs/tags/v1.8.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.8.3.rc1', sha256='011e99bc8674978e806c9fbb5c9866347e406ce3a7ec4b4fb9d4795652fbadfa')
    version('1.8.2',     sha256='9e053de1d6cdfa153d008baf9b4da2623d2950fc68222783788ce5c9c089349b',preferred=True)
    version('1.8.1',     sha256='927c0939ee26b394c5e50713f0cdc6c8c9eac9ddb9a28f1fe8ef97a89c533847')
    version('1.8.0',     sha256='7ea6aa49c8693ac536e9e1cff6b95a40d5732e6ec66daab6f91771aa12dbbf81')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-pyyaml',type='run')
    depends_on('py-requests',type='run')
    depends_on('py-distro',type='run')

    # depends_on('py-foo',        type=('build', 'run'))

    def patch(self):
        filter_file(r'LAST_TAG',"{}".format(self.version),'setup.py')

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
