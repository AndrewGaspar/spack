# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBootstrap140(RustBootstrapPackage):
    """Rust 1.40"""

    maintainers = ['AndrewGaspar']

    version('1.40.0', sha256='dd97005578defc10a482bff3e4e728350d2099c60ffcf1f5e189540c39a549ad')

    depends_on('rust-can-bootstrap-1-40')
    provides('rust-can-bootstrap-1-41')
