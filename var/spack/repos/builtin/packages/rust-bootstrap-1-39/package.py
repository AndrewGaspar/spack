# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBootstrap139(RustBootstrapPackage):
    """Rust 1.39"""

    maintainers = ['AndrewGaspar']

    version('1.39.0', sha256='b4a1f6b6a93931f270691aba4fc85eee032fecda973e6b9c774cd06857609357')

    depends_on('rust-can-bootstrap-1-39', type='build')
    provides('rust-can-bootstrap-1-40')
