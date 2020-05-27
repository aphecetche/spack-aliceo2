# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPythonGnureadline(PythonPackage):
    """The standard Python readline extension statically linked against the GNU readline library, providing readline support to Python on platforms without it. http://pypi.python.org/pypi/gnureadline"""

    url      = "https://github.com/ludwigschwardt/python-gnureadline/archive/v8.0.0.tar.gz"

    version('8.0.0',   sha256='10f0b92b7a9f9623ada5dfa7ec12e9a22b6b96de0f9960d17225ccb6252ccea7')
    version('6.3.8',   sha256='2a9ee5d4d1c82a899249a2e1f2073e01fb3f7ff6a7b58e5022d19bad0606818a')
    version('6.3.3',   sha256='87ebb0f528b05d4d76d6e623d4ae348e26cba7dd5f115e1eacf23746808ed140')
    version('6.2.5',   sha256='36f547bb60ca63051bd796da0c09fca68d96ab52b144cf280e3960637f7ae853')
    version('6.2.4.1', sha256='fd301dad55954cabef9589eb7cbc9d82fedfcdbef637305f3ac1ad446e1af301')
    version('6.2.4',   sha256='78e044ef1a554e32c5f8fed874133df77420aa632dd79394b2ed776fa55abcc5')
    version('6.2.2',   sha256='089d5a676462b165c9666d6eaa96785d06a39e1cf24dc9a42b08cdf6dad60ac7')
    version('6.2.1',   sha256='5700b6fc26007a1525ff1ccf2a757954165b9cf8440ef86b27b310851709c6ba')
    version('6.2.0',   sha256='74981041031f66822049564df12a3aa7bb014aba48161f7d1b4654722b819a6a')
    version('6.1.0',   sha256='ac8325ed4166e98ff15137b710cad520615641dffc20f70b9f72d55d1591cc21')

    depends_on('py-setuptools', type='build')

    def build_args(self, spec, prefix):
        args = []
        return args
