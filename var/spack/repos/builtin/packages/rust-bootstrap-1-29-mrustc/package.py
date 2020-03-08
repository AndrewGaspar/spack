# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from shutil import copyfile

from spack import *


class RustBootstrap129Mrustc(Package):
    "mrustc is a minimal C++ implementation of the Rust toolchain"

    homepage = "https://github.com/thepowersgang/mrustc"
    url = "https://github.com/thepowersgang/mrustc/archive/v0.8.0.tar.gz"

    maintainers = ['AndrewGaspar']

    version('0.9',   sha256='381ded90498a04a667ab67a33c1bf7ff1269026bd45a6bde9bac8bf694929de6')

    resource(
        name='rustc-1.29.0-src',
        url='https://static.rust-lang.org/dist/rustc-1.29.0-src.tar.gz',
        sha256='a4eb34ffd47f76afe2abd813f398512d5a19ef00989d37306217c9c9ec2f61e9',
        placement='rustc-1.29.0-src'
    )

    depends_on('cmake', type='build')
    depends_on('binutils', type='build')
    depends_on('python@:2.8', type='build')
    depends_on('openssl')
    depends_on('libssh2')
    depends_on('libgit2')

    provides('rust-can-bootstrap-1-30')

    def patch(self):
        # raise InstallError('cwd: ' + os.getcwd())
        # Apply the source patch
        patch = which("patch", required=True)
        patch(
            '-s',
            '-p0',
            '-i', '../rustc-1.29.0-src.patch',
            '-d', './rustc-1.29.0-src')

    def install(self, spec, prefix):
        make(
            '-f', 'minicargo.mk',
            'output/rustc',
            'output/cargo',
            extra_env={
                # vendored libgit2 wasn't correctly building (couldn't find the
                # vendored libssh2), so let's just have spack build it
                'LIBSSH2_SYS_USE_PKG_CONFIG': '1',
                'LIBGIT2_SYS_USE_PKG_CONFIG': '1'
            }
        )

        make(
            '-C', 'run_rustc',
            'output/prefix/bin/rustc',
            'output/prefix/bin/cargo',
            'output/prefix/lib/rustlib/x86_64-unknown-linux-gnu/lib/libstd.rlib',
            extra_env={
                # vendored libgit2 wasn't correctly building (couldn't find
                # the vendored libssh2), so let's just have spack build it
                'LIBSSH2_SYS_USE_PKG_CONFIG': '1',
                'LIBGIT2_SYS_USE_PKG_CONFIG': '1'
            }
        )
        
        install_tree('run_rustc/output/prefix', prefix)
        copyfile(prefix.bin.rustc_binary, prefix.bin.rustc)

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path(
            'LD_LIBRARY_PATH',
            join_path(
                self.prefix,
                'lib/rustlib/x86_64-unknown-linux-gnu/lib'))

    def setup_dependent_run_environment(self, env, dependent_spec):
        env.prepend_path(
            'LD_LIBRARY_PATH',
            join_path(
                self.prefix,
                'lib/rustlib/x86_64-unknown-linux-gnu/lib'))