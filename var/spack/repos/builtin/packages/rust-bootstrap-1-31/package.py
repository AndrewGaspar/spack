# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBootstrap131(RustBootstrapPackage):
    """Rust 1.31"""

    maintainers = ['AndrewGaspar']

    version('1.31.1', sha256='91d2fc22f08d986adab7a54eb3a6a9b99e490f677d2d092e5b9e4e069c23686a')

    depends_on('rust-can-bootstrap-1-31', type='build')
    provides('rust-can-bootstrap-1-32')

    variant(
        'mrustc',
        default=False, description='Prefer bootstrapping from mrustc')
    depends_on('rust-bootstrap-1-30 +mrustc', type='build', when='+mrustc')
