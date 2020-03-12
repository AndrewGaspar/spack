# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBinaryPowerpc64leUnknownLinuxGnu(RustBinaryPackage):
    """Install Rust binary distributions for powerpc64le-unknown-linux-gnu"""

    homepage = "https://www.rust-lang.org/"

    maintainers = ['AndrewGaspar']

    rust_target_arch = 'powerpc64le-unknown-linux-gnu'

    version('1.42.0', sha256='805b08fa1e0aad4d706301ca1f13e2d80810d385cece2c15070360b3c4bd6e4a')
    version('1.41.1', sha256='f9b53ca636625b3a2dd87600b6274223c11f866c9b5a34b638ea0013186659d3')
    version('1.41.0', sha256='ba231b0d8273d6928f61e2be3456e816a1de8050135e20c0623dc7a6ea03ba68')
    version('1.40.0', sha256='b1a23e35c383f99e647df6a9239b1dc9313e293deb70a76ba58e8ebe55ef623b')
    version('1.39.0', sha256='53b3fd942c52709f7e6fe11ea572d086e315a57a40b84b9b3290ac0ec8c7c84a')
    version('1.38.0', sha256='f9ed1bb6525abdd4dd6ef10782ad45d2f71496e0c3c88e806b510c81a91c4ff7')
    version('1.37.0', sha256='27c59ec40e9e9f71490dc00bf165156ae3ea77c20ffa4b5e5fd712e67527b477')
    version('1.36.0', sha256='654a7a18d881811c09f630b0c917825b586e94a6142eceaede6b8046718e4054')
    version('1.35.0', sha256='a933955adec386d75d126e78df5b9941936e156acb3353fc44b85995a81c7bb2')
    version('1.34.2', sha256='4ddd55014bbd954b3499859bfa3146bff471de21c1d73fc6e7cccde290fc1918')
    version('1.34.1', sha256='94ac92d08afcfa2d77ae207e91b57c00cb48ff7ba08a27ed3deb2493f33e8fb1')
    version('1.34.0', sha256='3027e87802e161cce6f3a23d961f6d73b9ed6e829b2cd7af5dfccf6e1207e552')
    version('1.33.0', sha256='db885aa4c2c6896c85257be2ade5c9edea660ca6878970683e8d5796618329b5')
    version('1.32.0', sha256='d6d5c9154f4459465d68ebd4fa1e17bad4b6cfe219667dddd9123c3bfb5dd839')
    version('1.31.1', sha256='a6f61b7a8a06a2b0a785391cc3e6bb8004aa72095eea80db1561039f5bb3e975')
    version('1.30.1', sha256='a7d4806e6702bdbad5017eeddc62f7ff7eb2438b1b9c39cbc90c2b1207f8e65f')
    version('1.30.0', sha256='0b53e257dc3d9f3d75cd97be569d3bf456d2c0af57ed0bd5e7a437227d8f465a')
    version('1.29.2', sha256='344003b808c20424c4699c9452bd37cdee23857dd4aa125e67d1d6e4bc992091')
    version('1.29.1', sha256='26a6d652ade6b6a96e6af18e846701ee28f912233372dfe15432139252f88958')
    version('1.29.0', sha256='d6954f1da53f7b3618fba3284330d99b6142bb25d9febba6dbfedad59ca53329')
    version('1.28.0', sha256='255818156ec1f795ed808a44b4fdb8019187d5ebb7f837ae8f55a1ca40862bb6')
    version('1.27.2', sha256='11034d150e811d4903b09fd42f0cb76d467a6365a158101493405fff1054572f')
    version('1.27.1', sha256='a08e6b6fed3329fcd1220b2ee4cd7a311d99121cf780fb6e1c6353bfeddfb176')
    version('1.27.0', sha256='847774a751e848568215739d384e3baf4d6ec37d27fb3add7a8789208c213aff')
    version('1.26.2', sha256='ea045869074ae3617eeb51207ce183e6915784b9ed615ecb92ce082ddb86ec1f')
    version('1.26.1', sha256='ad8b2f6dd8c5cca1251d65b75ed2120aae3c5375d2c8ed690259cf4a652d7d3c')
    version('1.26.0', sha256='3ba3a4905730ec01007ca1096d9fc3780f4e81f71139a619e1f526244301b7f4')
    version('1.25.0', sha256='79eeb2a7fafa2e0f65f29a1dc360df69daa725347e4b6a533684f1c07308cc6e')
    version('1.24.1', sha256='6f6c4bebbd7d6dc9989bf372c512dea55af8f56a1a0cfe97784667f0ac5430ee')
    version('1.24.0', sha256='25d9b965a63ad2f345897028094d4c7eafa432237b478754ccbcc299f80629c8')
    version('1.23.0', sha256='60f1a1cc182c516de08c1f42ada01604a3d94383e9dded6b237ae2233999437b')
    version('1.22.1', sha256='b0c5149c16ce705c572b4c0976dd5c197309f12dda313f83a10e4f0a979eea6c')
    version('1.22.0', sha256='1fb64fc8f76ca8ae00fcc57774f1fb2e3517b46000f44cd7e50246ed90ecb976')
    version('1.21.0', sha256='67d4a1c5ed3c19168ca5fee799fc6a153a9b45d88e4351723fc41f409f87bec9')
    version('1.20.0', sha256='cf5be95e2f8212b5231b175d2d2572fdf55a637997655eef460fdeec2ed6d349')
    version('1.19.0', sha256='9ca374e9ea1e5f33394d2a8278591def523cbf05ec0ecfa966673f10b72c035c')
    version('1.18.0', sha256='62cae76530faccf51ac8f92c1e65a9c3823465088bf4e6fdf0ece4197e74f5a3')
    version('1.17.0', sha256='2dda1fff20aecd7b208babfd45f70c608978fe2594916d1448e42757bb7e759f')
    version('1.16.0', sha256='4a6fcf1f6a015b9809e2fa7d3b35d117364e95df21a890089c8f5c06e252b7a5')
    version('1.15.1', sha256='3f40285145ad3b7cde703b18ac9c57bafb482c636da26d65f54abbf369b013cb')
    version('1.15.0', sha256='b3d50b34d464ee1adb56b7924499eb619153fd486ea07a3400067725d119a0c5')
    version('1.14.0', sha256='d3956c671b35fb43e6ebd1757719f862d7c700c223b65fa61bdf628ced81b3af')
