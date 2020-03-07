# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack import *


class RustBootstrap129Mrustc(Package):
    "Builds Rust 1.29 Using MRustc"

    homepage = "https://www.rust-lang.org/"
    url      = "https://static.rust-lang.org/dist/rustc-1.29.2-src.tar.gz"

    maintainers = ['AndrewGaspar']

    version('1.29.2', sha256='5088e796aa2e47478cdf41e7243fc5443fafab0a7c70a11423e57c80c04167c9')

    depends_on('cmake', type='build')
    depends_on('binutils', type='build')
    depends_on('python@:2.8', type='build')
    depends_on('mrustc +mrustc +minicargo', type='build')
    depends_on('openssl')
    depends_on('libssh2')
    depends_on('libgit2')

    provides('rust-can-bootstrap-1-30')

    def install(self, spec, prefix):
        # Emplace the lib/librustc_macro re-implementation from mrustc
        mkdirp('lib')
        install_tree(spec['mrustc'].prefix.lib, 'lib')

        # Apply the source patch
        patch = which("patch", required=True)
        patch(
            '-s',
            '-p0',
            '-i', join_path(spec['mrustc'].prefix, 'rustc-1.29.0-src.patch'))

        make(
            '-f', join_path(spec['mrustc'].prefix.share, 'minicargo.mk'),
            'RUSTCSRC=./',
            'RUSTC_VERSION=1.29.0',
            'MRUSTC=%s' % join_path(spec['mrustc'].prefix.bin, 'mrustc'),
            'MINICARGO=%s'
            % join_path(spec['mrustc'].prefix.tools.bin, 'minicargo'),
            'OVERRIDE_DIR=%s'
            % join_path(
                spec['mrustc'].prefix,
                'script-overrides/stable-1.29.0-linux/'),
            'output/rustc',
            'output/cargo',
            extra_env={
                # vendored libgit2 wasn't correctly building (couldn't find the
                # vendored libssh2), so let's just have spack build it
                'LIBSSH2_SYS_USE_PKG_CONFIG': '1',
                'LIBGIT2_SYS_USE_PKG_CONFIG': '1'
            }
        )

        install_tree(spec['mrustc'].prefix.run_rustc, 'run_rustc')

        # pushd
        cwd = os.getcwd()
        os.chdir('run_rustc')

        try:
            make(
                'RUST_SRC=..',
                'RUSTC_VERSION=1.29.0',
                'PREFIX={}'.format(prefix),
                extra_env={
                    # vendored libgit2 wasn't correctly building (couldn't find
                    # the vendored libssh2), so let's just have spack build it
                    'LIBSSH2_SYS_USE_PKG_CONFIG': '1',
                    'LIBGIT2_SYS_USE_PKG_CONFIG': '1'
                }
            )
        finally:
            #popd
            os.chdir(cwd)
