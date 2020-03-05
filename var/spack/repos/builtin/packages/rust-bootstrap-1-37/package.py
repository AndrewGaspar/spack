# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBootstrap137(RustBootstrapPackage):
    """Rust 1.37"""

    maintainers = ['AndrewGaspar']

    version('1.37.0', sha256='120e7020d065499cc6b28759ff04153bfdc2ac9b5adeb252331a4eb87cbe38c3')

    depends_on('rust-can-bootstrap-1-37', type='build')
    provides('rust-can-bootstrap-1-38')
