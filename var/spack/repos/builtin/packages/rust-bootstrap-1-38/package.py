# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBootstrap138(RustBootstrapPackage):
    """Rust 1.38"""

    maintainers = ['AndrewGaspar']

    version('1.38.0', sha256='644263ca7c7106f8ee8fcde6bb16910d246b30668a74be20b8c7e0e9f4a52d80')

    depends_on('rust-can-bootstrap-1-38', type='build')
    provides('rust-can-bootstrap-1-39')
