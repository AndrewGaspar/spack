# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBootstrap134(RustBootstrapPackage):
    """Rust 1.34"""

    maintainers = ['AndrewGaspar']

    version('1.34.2', sha256='c69a4a85a1c464368597df8878cb9e1121aae93e215616d45ad7d23af3052f56')
    version('1.34.1', sha256='b0c785264d17e1dac4598627c248a2d5e07dd39b6666d1881fcfc8e2cf4c40a7')
    version('1.34.0', sha256='7ac85acffd79dd3a7c44305d9eaabd1f1e7116e2e6e11e770e4bf5f92c0f1f59')

    depends_on('rust-can-bootstrap-1-34', type='build')
    provides('rust-can-bootstrap-1-35')
