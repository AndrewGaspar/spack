# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBootstrap132(RustBootstrapPackage):
    """Rust 1.32"""

    maintainers = ['AndrewGaspar']

    version('1.32.0', sha256='4c594c7712a0e7e8eae6526c464bf6ea1d82f77b4f61717c3fc28fb27ba2224a')

    depends_on('rust-can-bootstrap-1-32', type='build')
    provides('rust-can-bootstrap-1-33')

    variant(
        'mrustc',
        default=False, description='Prefer bootstrapping from mrustc')
    depends_on('rust-bootstrap-1-31 +mrustc', type='build', when='+mrustc')
