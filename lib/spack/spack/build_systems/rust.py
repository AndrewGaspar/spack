# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.directives import depends_on
from spack.package import PackageBase
from spack.util.executable import Executable, which
from spack.installer import InstallError


class RustBinaryPackage(PackageBase):
    """Specialized class for rust binary distributions.

    This class provides the common implementation for installing the official
    Rust binary distributions across architectures. Because the binary
    distributions are different between architectures, we need separate
    packages to provide each architecture. As of this writing, there's no way
    to provide distinct "versions" in a single package for different
    architectures.
    """

    # Only need an install phase
    phases = ['install']

    #: This attribute is used in UI queries that need to know the build
    #: system base class
    build_system_class = 'RustBinaryPackage'

    # Specified by package - this is the target architecture used by Rust.
    rust_target_arch = None

    def url_for_version(self, version):
        url = "https://static.rust-lang.org/dist/rust-{0}-{1}.tar.gz"
        return url.format(version, self.rust_target_arch)

    def install(self, spec, prefix):
        install = Executable('./install.sh')
        install('--prefix=%s' % prefix)


class RustBootstrapPackage(PackageBase):
    """Specialized class for stages in the Rust bootstrapping process.

    The Rust compiler is written in Rust, which, of course, means that you
    can't easily build any given Rust compiler with just the compilers that
    tend to ship with the system.

    However, each public release of the Rust compiler can build itself and the
    next public release of the Rust compiler. This gives us a bootstrapping
    path from a binary distribution of the Rust compiler for all platforms that
    Rust supports. Additionally, a primitive C++ implementation of the Rust
    compiler, mrustc, exists that, as of this writing, can build version 1.29
    of the Rust compiler for x86. This gives you the ability to bootstrap the
    latest release of the Rust compiler from a C++ compiler on x86 platforms.

    Since a package can never depend on itself, we can't represent the
    bootstrapping chain using a single package. Instead, we need each step in
    the chain to be a distinct package. This base class attempts to solve this
    by making it easy to introduce each stage in the process, while also
    supporting "off ramps" to mrustc.
    """

    # All RustBootstrapPackage packages have the same homepage and URL.
    homepage = "https://www.rust-lang.org/"
    url      = "https://static.rust-lang.org/dist/rustc-1.41.0-src.tar.gz"

    phases = ['configure', 'build', 'install']

    #: This attribute is used in UI queries that need to know the build
    #: system base class
    build_system_class = 'RustBootstrapPackage'

    # indicates if this is a terminal package in the Rust bootstrap process.
    # Practically, rust-bootstrap is final_bootstrap, but rust-bootstrap-* are
    # not.
    final_bootstrap = False

    depends_on('cmake', type='build')
    # We don't use binutils on Mac - we pick up ar either from the system or
    # compiler
    depends_on('binutils', type='build', when='platform=linux')
    depends_on('binutils', type='build', when='platform=cray')
    depends_on('python@:2.8', type='build')
    depends_on('openssl')
    depends_on('libssh2')
    depends_on('libgit2')

    def configure(self, spec, prefix):
        if self.spec.satisfies('platform=linux target=x86_64:') or \
           self.spec.satisfies('platform=cray target=x86_64:'):
            target = 'x86_64-unknown-linux-gnu'
        elif self.spec.satisfies('platform=linux target=ppc64le:'):
            target = 'powerpc64le-unknown-linux-gnu'
        elif self.spec.satisfies('platform=darwin target=x86_64:'):
            target = 'x86_64-apple-darwin'
        else:
            raise InstallError(
                "rust-binary is not supported for '%s'"
                % self.spec.architecture)

        boot_bin = \
            spec[
                'rust-can-bootstrap-{0}'.format(
                    self.spec.version.up_to(2).dashed)
            ].prefix.bin

        # Always build rustc and cargo
        tools = ['rustc', 'cargo']
        if self.final_bootstrap:
            # Only make additional components available in 'rust-bootstrap'
            if '+rustfmt' in self.spec:
                tools.append('rustfmt')
            if '+analysis' in self.spec:
                tools.append('analysis')
            if '@1.33: +clippy' in self.spec:
                tools.append('clippy')
            if '+rls' in self.spec:
                tools.append('rls')
            if '+src' in self.spec:
                tools.append('src')

        ar = which('ar', required=True)

        with open('config.toml', 'w') as out_file:
            out_file.write("""\
[build]
cargo = "{cargo}"
rustc = "{rustc}"
docs = false
vendor = true
extended = true
verbose = 2
tools = {tools}

[rust]
channel = "stable"
rpath = true

[target.{target}]
ar = "{ar}"

[install]
prefix = "{prefix}"
sysconfdir = "etc"
""".format(
                cargo=boot_bin.cargo,
                rustc=boot_bin.rustc,
                prefix=prefix,
                target=target,
                ar=ar.path,
                tools=tools
            )
            )

    def build(self, spec, prefix):
        x_py = Executable('./x.py')
        x_py(
            'build',
            extra_env={
                # vendored libgit2 wasn't correctly building (couldn't find the
                # vendored libssh2), so let's just have spack build it
                'LIBSSH2_SYS_USE_PKG_CONFIG': '1',
                'LIBGIT2_SYS_USE_PKG_CONFIG': '1'
            })

    def install(self, spec, prefix):
        x_py = Executable('./x.py')
        x_py('install')
