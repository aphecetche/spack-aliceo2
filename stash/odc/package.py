# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Odc(CMakePackage):
    """The Online Device Control project control/communicate with a graph
    (topology) of FairMQ devices."""

    homepage = "https://github.com/FairRootGroup/ODC"
    url = "https://github.com/FairRootGroup/ODC/archive/refs/tags/0.36.tar.gz"
    git = "https://github.com/FairRootGroup/ODC.git"

    version('0.56', sha256='7d1bc49b67d6e3f004138a4e4969801cf6529ac822ddfc216bbbef85f17d3c4e')
    version('0.52', sha256='2c8e62fca4baf78bd72039c9277be346c98e3a0277fcd406b7d1cf9d05953aaf')
    version('0.36', sha256='04d0d94c55568bf084ba0ff575a7bdcd18761b43564845dda66866697dc6ccf3')

    variant('grpc_client',default=True,description='Build gRPC client')
    variant('grpc_server', default=True, description='Build gRPC server')
    variant('cli_server',default=True,description='Build CLI server')
    variant('examples',default=True,description='Build examples')
    variant('default_plugins',default=True,description='Build default plugins')
    variant('epn_plugin',default=True,description='Build EPN plugins')
    variant('infologger',default=False,description='Enable InfoLogger support')

    depends_on('grpc +codegen+shared',when='+grpc_client')
    depends_on('grpc +codegen+shared',when='+grpc_server')
    depends_on('protobuf',when='+grpc_client')
    depends_on('protobuf',when='+grpc_server')
    depends_on('o2-infologger',when='+infologger')
    depends_on('boost@1.67:')
    depends_on('dds@3.5.16:')
    depends_on('fairmq@1.4.26:')
    depends_on('fairlogger')
    depends_on('flatbuffers')
    depends_on('picosha2')

    depends_on('ninja',type='build')
    generator='Ninja'

    def patch(self):
      filter_file(r'\${PROJECT_VERSION} PARENT_SCOPE',
      '{} PARENT_SCOPE'.format(self.version),
      'cmake/ODCUtils.cmake')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("BUILD_GRPC_CLIENT","grpc_client"))
        args.append(self.define_from_variant("BUILD_GRPC_SERVER","grpc_server"))
        args.append(self.define_from_variant("BUILD_CLI_SERVER","cli_server"))
        args.append(self.define_from_variant("BUILD_EXAMPLES","examples"))
        args.append(self.define_from_variant("BUILD_DEFAULT_PLUGINS","default_plugins"))
        args.append(self.define_from_variant("BUILD_EPN_PLUGIN","epn_plugin"))
        args.append(self.define_from_variant("BUILD_INFOLOGGER","infologger"))
        args.append(self.define("BUILD_TESTS",self.run_tests))
        return args
