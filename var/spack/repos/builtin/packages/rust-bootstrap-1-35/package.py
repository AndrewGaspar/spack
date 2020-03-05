# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBootstrap135(RustBootstrapPackage):
    """Rust 1.35"""

    maintainers = ['AndrewGaspar']

    version('1.35.0', sha256='5a4d637a716bac18d085f44dd87ef48b32195f71b967d872d80280b38cff712d')

    depends_on('rust-can-bootstrap-1-35', type='build')
    provides('rust-can-bootstrap-1-36')
