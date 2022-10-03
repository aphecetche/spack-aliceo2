# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

# //Details about finding OpenGL
# FIND_PACKAGE_MESSAGE_DETAILS_OpenGL:INTERNAL=[/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX11.1.sdk/System/Library/Frameworks/OpenGL.framework][/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX11.1.sdk/System/Library/Frameworks/OpenGL.framework][c
# ][v()]
#

class AppleGlu(Package):

    homepage = ""

    has_code = False

    version('4.0.0')

    provides('glu')

    # Only supported on 'platform=darwin' and compiler=apple-clang
    conflicts('platform=linux')
    conflicts('platform=cray')
    conflicts('%gcc')
    conflicts('%clang')

    phases = []

    def setup_dependent_build_environment(self, env, dependent_spec):
        # we try to setup a build environment with enough hints
        # for the build system to pick up on the Apple framework version
        # of OpenGL.
        # - for a cmake build we actually needs nothing at all as
        # find_package(OpenGL) will do the right thing
        # - for the rest of the build systems we'll assume that
        # setting the C_INCLUDE_PATH will be enough for the compilation phase
        # and *** for the link phase.
        env.prepend_path("C_INCLUDE_PATH","/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX")
        env.set("SPACK_APPLE_GLU","1")

    @property
    def libs(self):
        # OPENGL_glu_LIBRARY:FILEPATH=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX11.1.sdk/System/Library/Frameworks/OpenGL.framework
        return LibraryList('/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/Frameworks/OpenGL.framework')
