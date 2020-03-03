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
    url      = "https://static.rust-lang.org/dist/rustc-1.29.2-src.tar.gz"

    maintainers = ['AndrewGaspar']

    version('1.29.2', sha256='5088e796aa2e47478cdf41e7243fc5443fafab0a7c70a11423e57c80c04167c9')

    depends_on('cmake', type='build')
    depends_on('binutils', type='build')
    depends_on('python@:2.8', type='build')
    depends_on('mrustc +mrustc +minicargo', type='build')
    depends_on('openssl')

    def install(self, spec, prefix):
        make(
            '-f', join_path(spec['mrustc'].prefix.share, 'minicargo.mk'),
            'RUSTCSRC=./',
            'RUSTC_VERSION=1.29.0',
            'MRUSTC=%s' % join_path(spec['mrustc'].prefix.bin, 'mrustc'),
            'MINICARGO=%s' % join_path(spec['mrustc'].prefix.tools.bin, 'minicargo'),
            'output/rustc',
            'output/cargo'
        )

        # FIXME: This needs to self-bootstrap to a Rust 1.29 compiler built with 1.29
        mkdirp(prefix.bin)
        install('output/rustc', prefix.bin)
        install('output/cargo', prefix.bin)
