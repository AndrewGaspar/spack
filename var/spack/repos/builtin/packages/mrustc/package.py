# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from shutil import copyfile

class Mrustc(Package):
    "mrustc is a minimal C++ implementation of the Rust toolchain"

    homepage = "https://github.com/thepowersgang/mrustc"
    url = "https://github.com/thepowersgang/mrustc/archive/v0.8.0.tar.gz"

    maintainers = ['AndrewGaspar']

    version('0.9',   sha256='381ded90498a04a667ab67a33c1bf7ff1269026bd45a6bde9bac8bf694929de6')
    version('0.8.1', sha256='5c02feaa2094d8180eb11458ee4c2100ef84c51fda132a9c3d6c9fdcea3b82a8')
    version('0.8.0', sha256='50eeae45bffb118a515a3d735975ff030c8a67c6732af5baf1600f5e123282d6')

    variant('minicargo', default=True, description='Builds minicargo, a limited version of cargo')
    variant('mrustc', default=True, description='Builds mrustc, a limited version of rustc')

    def install(self, spec, prefix):
        mkdirp(prefix.bin)

        if '+mrustc' in self.spec:
            make('bin/mrustc')
            install('bin/mrustc', prefix.bin)

        if '+minicargo' in self.spec:
            make('-f', 'minicargo.mk', 'tools/bin/minicargo')
            install('tools/bin/minicargo', prefix.bin)
