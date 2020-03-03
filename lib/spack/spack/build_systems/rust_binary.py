# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import PackageBase
from spack.util.executable import Executable

class RustBinaryPackage(PackageBase):
    """Specialized class for rust binary distributions.

    This class provides the common implementation for installing the official
    Rust binary distributions across architectures. Because the binary
    distributions are different between architectures, then we need separate
    packages to provide each architecture.
    """

    # Only need an install phase
    phases = ['install']
    
    #: This attribute is used in UI queries that need to know the build
    #: system base class
    build_system_class = 'RustBinaryPackage'

    # Specified by package - this is the target architecture used by Rust.
    rust_target_arch = ''

    def url_for_version(self, version):
        url = "https://static.rust-lang.org/dist/rust-{0}-{1}.tar.gz"
        return url.format(version, self.rust_target_arch)

    def install(self, spec, prefix):
        install = Executable('./install.sh')
        install('--prefix=%s' % prefix)
