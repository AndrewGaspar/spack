# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBootstrap133(RustBootstrapPackage):
    """Rust 1.33"""

    maintainers = ['AndrewGaspar']

    version('1.33.0', sha256='5a01a8d7e65126f6079042831385e77485fa5c014bf217e9f3e4aff36a485d94')

    depends_on('rust-can-bootstrap-1-33', type='build')
    provides('rust-can-bootstrap-1-34')
