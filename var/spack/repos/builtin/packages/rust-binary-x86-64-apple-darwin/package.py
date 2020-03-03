# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBinaryX8664AppleDarwin(RustBinaryPackage):
    """Install Rust binary distributions for x86_64-apple-darwin"""

    homepage = "https://www.rust-lang.org/"

    maintainers = ['AndrewGaspar']

    rust_target_arch = 'x86_64-apple-darwin'

    version('1.41.1', sha256='16615288cf74239783de1b435d329f3d56ed13803c7c10cd4b207d7c8ffa8f67')
    version('1.41.0', sha256='b6504003ab70b11f278e0243a43ba9d6bf75e8ad6819b4058a2b6e3991cc8d7a')
    version('1.40.0', sha256='749ca5e0b94550369cc998416b8854c13157f5d11d35e9b3276064b6766bcb83')
    version('1.39.0', sha256='3736d49c5e9592844e1a5d5452883aeaf8f1e25d671c1bc8f01e81c1766603b5')
    version('1.38.0', sha256='bd301b78ddcd5d4553962b115e1dca5436dd3755ed323f86f4485769286a8a5a')
    version('1.37.0', sha256='b2310c97ffb964f253c4088c8d29865f876a49da2a45305493af5b5c7a3ca73d')
    version('1.36.0', sha256='91f151ec7e24f5b0645948d439fc25172ec4012f0584dd16c3fb1acb709aa325')
    version('1.35.0', sha256='ac14b1c7dc330dcb53d8641d74ebf9b32aa8b03b9d650bcb9258030d8b10dbd6')
    version('1.34.2', sha256='6fdd4bf7fe26dded0cd57b41ab5f0500a5a99b7bc770523a425e9e34f63d0fd8')
    version('1.34.1', sha256='f4e46b9994ccfab4a84059298d1dc8fd446b1bbb7449462e0459948f7debea0e')
    version('1.34.0', sha256='e6bea8d865cc7341c17fa3b8f25f7989e6b04f53e9da24878addc524f3a32664')
    version('1.33.0', sha256='864e7c074a0b88e38883c87c169513d072300bb52e1d320a067bd34cf14f66bd')
    version('1.32.0', sha256='f0dfba507192f9b5c330b5984ba71d57d434475f3d62bd44a39201e36fa76304')
    version('1.31.1', sha256='8398b1b303bdf0e7605d08b87070a514a4f588797c6fb3593718cb9cec233ad6')
    version('1.30.1', sha256='3ba1704a7defe3d9a6f0c1f68792c084da83bcba85e936d597bac0c019914b94')
    version('1.30.0', sha256='07008d90932712282bc599f1e9a226e97879c758dc1f935e6e2675e45694cc1b')
    version('1.29.2', sha256='63f54e3013406b39fcb5b84bcf5e8ce85860d0b97a1e156700e467bf5fb5d5f2')
    version('1.29.1', sha256='07b07fbd6fab2390e19550beb8008745a8626cc5e97b72dc659061c1c3b3d008')
    version('1.29.0', sha256='28a0473637585742f6d80ccd8afd88b6b400e65d623c33cb892412759444da93')
    version('1.28.0', sha256='5d7a70ed4701fe9410041c1eea025c95cad97e5b3d8acc46426f9ac4f9f02393')
    version('1.27.2', sha256='30c5cc58759caa4efdf2ea7d8438633139c98bee3408beb29ceb26985f3f5f70')
    version('1.27.1', sha256='475be237962d6aef1038a2faada26fda1e0eaea5d71d6950229a027a9c2bfe08')
    version('1.27.0', sha256='a1d48190992e01aac1a181bce490c80cb2c1421724b4ff0e2fb7e224a958ce0f')
    version('1.26.2', sha256='f193705d4c0572a358670dbacbf0ffadcd04b3989728b442f4680fa1e065fa72')
    version('1.26.1', sha256='ebf898b9fa7e2aafc53682a41f18af5ca6660ebe82dd78f28cd9799fe4dc189a')
    version('1.26.0', sha256='38708803c3096b8f101d1919ee2d7e723b0adf1bc1bb986b060973b57d8c7c28')
    version('1.25.0', sha256='fcd0302b15e857ba4a80873360cf5453275973c64fa82e33bfbed02d88d0ad17')
    version('1.24.1', sha256='9d4aacdb5849977ea619d399903c9378163bd9c76ea11dac5ef6eca27849f501')
    version('1.24.0', sha256='1aecba7cab4bc1a9e0e931c04aa00849e930b567d243da7b676ede8f527a2992')
    version('1.23.0', sha256='9274e977322bb4b153f092255ac9bd85041142c73eaabf900cb2ef3d3abb2eba')
    version('1.22.1', sha256='c7cf38a9fe56cc03b61213899e0e2db2153ce4c69ed36b794264c5d3629dae57')
    version('1.22.0', sha256='dcd0693666dbf595212323a2ee7c14bbe4ff94b527742a378be0482753ff99f2')
    version('1.21.0', sha256='75a7f4bd7c72948030bb9e421df27e8a650dea826fb5b836cf59d23d6f985a0d')
    version('1.20.0', sha256='fa1fb8896d5e327cbe6deeb50e6e9a3346de629f2e6bcbd8c10f19f3e2ed67d5')
    version('1.19.0', sha256='5c668fb60a3ba3e97dc2cb8967fc4bb9422b629155284dcb89f94d116bb17820')
    version('1.18.0', sha256='30f210e3133121812d74995a2831cfb3fe79c271b3cb1721815943bd4f7eb297')
    version('1.17.0', sha256='1689060c07ec727e9756f19c9373045668471ab56fd8f53e92701150bbe2032b')
    version('1.16.0', sha256='2d08259ee038d3a2c77a93f1a31fc59e7a1d6d1bbfcba3dba3c8213b2e5d1926')
    version('1.15.1', sha256='38606e464b31a778ffa7d25d490a9ac53b472102bad8445b52e125f63726ac64')
    version('1.15.0', sha256='8b02c3714d30a6111af805d76df0de28c045f883a9171839ebd5667327f2e50a')
    version('1.14.0', sha256='3381341524b0184da5ed2cdcddc2a25e2e335e87f1cf676f64d98ee5e6479f20')
    version('1.13.0', sha256='f538ca5732b844cf7f00fc4aaaf200a49a845b58b4ec8aef38da0b00e2cf6efe')
    version('1.12.1', sha256='0ac5e58dba3d24bf09dcc90eaac02d2df053122b0def945ec4cfe36ac6d4d011')
    version('1.12.0', sha256='608c4530dcbd2e29c9600a0743b1a83a62556c9525385a7e1a7ba4aa1467a132')
    version('1.11.0', sha256='2cdbc47438dc86ecaf35298317b77d735956eb160862e3f6d0fda0da656ecc35')
    version('1.10.0', sha256='4bb71249f4afd7cee07f63d681f9fcb1b525ee3dfd49722adab7a40024e45af7')
    version('1.9.0',  sha256='d59b5509e69c1cace20a57072e3b3ecefdbfd8c7e95657b0ff2ac10aa1dfebe6')
    version('1.8.0',  sha256='606bfa2ac277f2f37be1bbd4fd933f7820c8ed7b39efe8f58c1063e9a31d326e')
    version('1.7.0',  sha256='9642c62bba6d47a6103729d5617f031ce61b68d34735a9873fa99f7d8769cce4')
    version('1.6.0',  sha256='8c6897ed37ef6fd2890b176afa65306cc8943e3c770c9530a701f1aefd3942b1')
    version('1.5.0',  sha256='bad9d1a96bd423662f247ae9dd5f61846aae668ad2b8c332e72a8cf407f473e4')
    version('1.4.0',  sha256='7256617aec7c106be2aa3c5df0a2e613b13ec55e6237ab612bb4164719e09e21')
    version('1.3.0',  sha256='bfeac876e22cc5fe63a250644ce1a6f3892c13a5461131a881419bd06fcb2011')
    version('1.2.0',  sha256='0d471e672fac5a450ae5507b335fda2efc0b22ea9fb7f215c6a9c466dafa2661')
    version('1.1.0',  sha256='ac802916da3f9c431377c00b864a517bc356859495b7a8a123ce2c532ee8fa83')
    version('1.0.0',  sha256='4b18ea61f2fda53d0f2e59ddf651e96a08ed31205db15e82fa514d434c5594d8')
