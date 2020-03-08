# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBootstrap136(RustBootstrapPackage):
    """Rust 1.36"""

    maintainers = ['AndrewGaspar']

    version('1.36.0', sha256='04c4e4d7213d036d6aaed392841496d272146312c0290f728b7400fccd15bb1b')

    depends_on('rust-can-bootstrap-1-36', type='build')
    provides('rust-can-bootstrap-1-37')

    variant(
        'mrustc',
        default=False, description='Prefer bootstrapping from mrustc')
    depends_on('rust-bootstrap-1-35 +mrustc', type='build', when='+mrustc')
