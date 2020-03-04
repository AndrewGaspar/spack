# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBootstrap(Package):
    """Bootstrap the Rust compiler"""

    homepage = "https://www.rust-lang.org/"
    url      = "https://static.rust-lang.org/dist/rustc-1.41.0-src.tar.gz"

    maintainers = ['AndrewGaspar']

    phases = ['configure', 'build', 'install']

    version('1.41.0')

    depends_on('rust-binary@1.40.0:', type='build')
    depends_on('cmake', type='build')
    depends_on('binutils', type='build')
    depends_on('python@:2.8', type='build')
    depends_on('openssl')
    depends_on('libssh2')
    depends_on('libgit2')

    # rust-lang provides a specific version of the _language_. New versions
    # of the compiler can provide old versions of the language. E.g., rust
    # version 1.41.0 provides support for every version of the language up
    # through 1.41.
    #
    # We assume minor versions don't introduce language changes.
    provides('rust-lang@:1.41', when="@1.41.0")
    # rust-compiler provides a specific version of the _compiler_.
    provides('rust-compiler@1.41.0', when="@1.41.0")

    def configure(self, spec, prefix):
        boot_bin = spec['rust-binary'].prefix.bin

        with open('config.toml', 'w') as out_file:
            out_file.write("""
[build]
cargo = '{cargo}'
rustc = '{rustc}'
docs = false
vendor = true
extended = true

[rust]
channel = stable

[install]
prefix = '{prefix}'
""".format(cargo=boot_bin.cargo, rustc=boot_bin.rustc, prefix=prefix)

    def build(self, spec, prefix):
        x_py = Executable('./x.py')
        x_py('build',
            extra_env = {
                # libgit2 wasn't correctly
                'LIBSSH2_SYS_USE_PKG_CONFIG': '1',
                'LIBGIT2_SYS_USE_PKG_CONFIG': '1'
            })


    def install(self, spec, prefix):
        x_py = Executable('./x.py')
        x_py('install')

