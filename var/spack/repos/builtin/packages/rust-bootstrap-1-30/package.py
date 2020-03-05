# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBootstrap130(RustBootstrapPackage):
    """Rust 1.30"""

    maintainers = ['AndrewGaspar']

    version('1.30.1', sha256='36a38902dbd9a3e1240d46ab0f2ca40d2fd07c2ab6508ed7970c6c4c036b5b29')
    version('1.30.0', sha256='cd0ba83fcca55b64c0c9f23130fe731dfc1882b73ae21bef96be8f2362c108ee')

    depends_on('rust-can-bootstrap-1-30', type='build')
    provides('rust-can-bootstrap-1-31')
