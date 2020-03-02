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
#     spack install rust-bootstrap-1-29
#
# You can edit this file again by typing:
#
#     spack edit rust-bootstrap-1-29
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class RustBootstrap129(Package):
    "Builds Rust 1.29"

    homepage = "https://www.rust-lang.org/"
    url      = "https://static.rust-lang.org/dist/rustc-1.29.0-src.tar.gz"

    maintainers = ['AndrewGaspar']

    # version('1.2.4')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make('install')
