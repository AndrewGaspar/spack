# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBootstrap141(RustBootstrapPackage):
    """Rust 1.41"""

    maintainers = ['AndrewGaspar']

    version('1.41.1', sha256='38c93d016e6d3e083aa15e8f65511d3b4983072c0218a529f5ee94dd1de84573')
    version('1.41.0', sha256='5546822c09944c4d847968e9b7b3d0e299f143f307c00fa40e84a99fabf8d74b')

    depends_on('rust-can-bootstrap-1-41', type='build')
    provides('rust-can-bootstrap-1-42')

    variant(
        'mrustc',
        default=False, description='Prefer bootstrapping from mrustc')
    depends_on('rust-bootstrap-1-40 +mrustc', type='build', when='+mrustc')
