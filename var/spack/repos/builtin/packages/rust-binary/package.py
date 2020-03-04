# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBinary(Package):
    """Indirection package for installing the correct rust binary distribution
    for the target platform
    """

    homepage = "https://www.rust-lang.org"
    # This release tar isn't actually even used, but we need something to
    # create unique hashes for each version
    url = "https://github.com/rust-lang/rust/archive/1.41.1.tar.gz"

    maintainers = ['AndrewGaspar']

    def install(self, spec, prefix):
        if self.spec.satisfies('platform=linux target=x86_64:') or \
           self.spec.satisfies('platform=cray target=x86_64:'):
            dep = 'rust-binary-x86-64-unknown-linux-gnu'
        elif self.spec.satisfies('platform=linux target=ppc64le:'):
            dep = 'rust-binary-powerpc64le-unknown-linux-gnu'
        elif self.spec.satisfies('platform=darwin target=x86_64:'):
            dep = 'rust-binary-x86-64-apple-darwin'
        else:
            raise InstallError(
                "rust-binary is not supported for '%s'"
                % self.spec.architecture)

        install_tree(spec[dep].prefix.bin, prefix.bin)
        install_tree(spec[dep].prefix.etc, prefix.etc)
        install_tree(spec[dep].prefix.lib, prefix.lib)
        install_tree(spec[dep].prefix.share, prefix.share)

    releases = [
        ('1.41.1', '68271e5cf4672b2b5d2048c202c6d04f98e24e5d39621696dc39dc1b7a0601bf'),
        ('1.41.0', '77996f7ef910d1c438f3c75cd21ff773b52a4aedaf0dd806f79ef239daf4638c'),
        ('1.40.0', 'c1fe30cb53760165cc1d513c5315355c978dc8eaf0a0bf7356877cfd9358c17d'),
        ('1.39.0', 'c2261f54f4b9e038712fd11f72f6583c12243f60fd9d2832eb6272ce8d804a5e'),
        ('1.38.0', '6f9762e091f645c7ec93fdd5a094f8af1176b519569f6a2dfd6c850cc0f471a0'),
        ('1.37.0', '6fd0af588b896e369e0a7cba84a54bfb4cd01628a3a9b5fb73dc43c2632e2a8b'),
        ('1.36.0', '6821f4260ac801e0837e70d80a989b736fad80d5cffbb043677c72cfa37eb4a4'),
        ('1.35.0', '1f6dc2c8994ca4388ae124917cfa98e6a4b8e03d9562c82212d6f1a6f2bc2b25'),
        ('1.34.2', '7baa5cc81ec36d17c8852ea24f8604ac042f524f96d55758b2d4ef0e34c0703d'),
        ('1.34.1', '0fb4a63d9ab7d37ddf1085846707f7c6f05dc8693bac5c20236c166368bd0ec4'),
        ('1.34.0', '5966fdef822a01ea7dcfb1894cbdb8a839516d2a3c7010dd2066199ad0b37a69'),
        ('1.33.0', '73ece803299c84b7841b1ef227a8bcc008468a4be058966e10ad143e7a3fdd58'),
        ('1.32.0', '3c1286650a9f15b41c3fe03e7f0b49ca92ce0f9383f9a5dfdf4f2e4ce768ac16'),
        ('1.31.1', '954342974ed53f366bfdd39c9b59d02beb949364985fd0dcf9a1b5919ed52341'),
        ('1.30.1', 'eb152bcfe3fa51fa7baaa898f341d3388eddde89145a790c890e756f54a1b755'),
        ('1.30.0', 'd4749ae0bbf94772998eed6be8585f08df27164402955729abfe69eefe0f9c3a'),
        ('1.29.2', 'aee5d4d2efd36b01641f653a84c9ba3be279a709c022c61041048b759071dcb6'),
        ('1.29.1', '2de90ad250ea3a58ea327a6b6654f5aff6e2c228a33cd56c91471ba34f1520ee'),
        ('1.29.0', '7689c95c0bab42e32eb82c1892785fe53faa8ae89a5c48bdfafb13a43ac8ec7e'),
        ('1.28.0', '9815d36b1289ff3e78a1aa427284f88e60c08c43bd8c351dab895a71f896b6ab'),
        ('1.27.2', 'c5871e9e13121749bf94223beb41e1ecbf427c0d780fbda3f6dc160ca153c407'),
        ('1.27.1', '05fc5cfef9f723f942d8c8db399902df69be0e47e8e4b19b55bceb5814a79367'),
        ('1.27.0', '0bbca54761be5302efc6e6fdb5f4dab4e0dec24458ca7c13538b7259885f9457'),
        ('1.26.2', '3afc81f36150232484cc848ca00ede758802964f7376c0a21a6c4661e0285f1b'),
        ('1.26.1', 'b609749195d10e3b5a979f5dc15fe9b6122562f37867432ba7d76d3b75276e5c'),
        ('1.26.0', '094de0ad1319f17b2caaf1cbb09c2b37f96fa920983cf901b181fd7c77f022da'),
        ('1.25.0', 'c67cb2501814cdf0062fd518e4bc950bb7bdb33fd4c8e6fb6e8ecd84d88390d7'),
        ('1.24.1', '5d0054a2edea8cdab2f390291bd5f272f76747980dff2e9640a6eb277c5e57f3'),
        ('1.24.0', '645fae208a07951722dec407eee0d1b4cc4bacb27f834aae60a0cbe30b9f8d36'),
        ('1.23.0', 'cc3f8ac5dd561768d93dba5941701df9fa5f0421caba2151869fbb4ad2143a64'),
        ('1.22.1', '5160a72127c899a79b35a40c45d2e3c3c739deaca71545fb4db6b6b84f25a8f7'),
        ('1.22.0', '33554829a6ac5b3432ecee38bb155b023ae73f80b8a70766155440161ad3faba'),
        ('1.21.0', 'a0e674cce176a5c90804d394e57887b278acfcdbda4fe0f2ae5876531a94faa4'),
        ('1.20.0', 'ca9307bf18a422029a1fca19ae1fa6c22e3047ff066fb041f9d0a9c886937860'),
        ('1.19.0', '7e1ecb476118b79b5abed02bc7a724bb65413057e26f1d2b8538c572f7463be0'),
        ('1.18.0', '77720ad4bf93175a73a94507fbf68c669bb66cf7c9a071f59a25510a4dfa1dbd'),
        ('1.17.0', '91c59dfc727dd56114b11badf60ada8338d6afd2a5fb797b1e1886ef60dd3fbe'),
        ('1.16.0', 'b7ec2d24d41ef2c27b1883d54f44a3c0a2eeecaf8c7abc1855f3171f3e0392cb'),
        ('1.15.1', 'c9e880a6eb72e9ec689139844ba82e956aad6d69f11e89114a47fb7858d2cef0'),
        ('1.15.0', '75e2e93da52950d4d8b0b68048045322dfd2b357aa9bd88bb6e91f814fbafeb2'),
        ('1.14.0', '3517ed84d1d407e3ee819298970d153e9922618295716bcc3ecaec35a8716ddf'),
        ('1.13.0', '41f30438ace67ef86be5a541b4b4c5ca25521b380d0f9b3daf8487de577bf563'),
        ('1.12.1', '9f4d6c71a2fe09991b7d4b1b3d78b4d3a0c8bdc5bdf39553c58bc59100c1ba4e'),
        ('1.12.0', 'ad79a747fd6edd99b2cbedb12f371eeae5120c9a9949d52a8838bf3caf950c86'),
        ('1.11.0', '5d7bd80eda9aca94e17ddd44181e37184c7f0b168f5be702fb2826b37d1e2be9'),
        ('1.10.0', 'f7eb1faf8d170ff066ecc8f66de1dbb65995a4fc3dcf3966a8d49a241be3d9bc'),
        ('1.9.0',  '817e4af3c1cc8185374d33104ac56f762afb737658e0ec61d20546683786e6c8'),
        ('1.8.0',  '5e93d68b753b3b434fcfe41d7e596d36b56a2032b1df573cf728a05cc18c85dc'),
        ('1.7.0',  'c8b22d117b015ff6b8a3340d96308873cb92dd78ca0bec50f5470f22580b4dd4'),
        ('1.6.0',  'bfe4215086b42a0f3142a04b65644524edcc3fa64da877be1ed0e306ecb8520e'),
        ('1.5.0',  'f3e553e956bc80a335aec508e933909861c69ec348e562586f4ebf72a86f32b6'),
        ('1.4.0',  '903425a68d05a42690236e10aef483fb32aa348d3909f728990ce786ae2f88a0'),
        ('1.3.0',  'e940ae35b6533e810329dc0e68817c6cf58883428649bd682df560a3dd0ea055'),
        ('1.2.0',  '6ce51fa1d741f96e7bba96fb9cdb3640128bc20d529092bc84ca0733e33177ac'),
        ('1.1.0',  'b4739703055ec5c2668be170faa2fac85c3660a93836fd09eebba0c60e878900'),
        ('1.0.0',  '761bb380a261a369e2af0cf23b7a03fbcf200cdea546daec20a528a529c1dfcf')
    ]

    for ver, hash in releases:
        version(ver, sha256=hash)
        current_ver = Version(ver)
        next_minor_ver = \
            Version('{}.{}'.format(current_ver[0], current_ver[1] + 1))
        # rust-lang provides a specific version of the _language_. New versions
        # of the compiler can provide old versions of the language. E.g., rust
        # version 1.41.0 provides support for every version of the language up
        # through 1.41.
        #
        # We assume minor versions don't introduce language changes.
        provides(
            'rust-lang@:{}'.format(current_ver.up_to(2)),
            when="@{}".format(ver))
        # rust-compiler provides a specific version of the _compiler_.
        provides('rust-compiler@{}'.format(ver), when="@{}".format(ver))
        # rust-binary can bootstrap itself and 1 minor version newer. It's
        # possible there's a more expansive matrix here, but somebody else will
        # need to figure out what that matrix is
        provides(
            'rust-can-bootstrap-{}'.format(next_minor_ver.up_to(2).dashed),
            when="@{}".format(ver))
        provides(
            'rust-can-bootstrap-{}'.format(current_ver.up_to(2).dashed),
            when="@{}".format(ver))

        depends_on('rust-binary-x86-64-unknown-linux-gnu@%s' % ver, when='@%s platform=linux target=x86_64:' % ver, type='build')
        depends_on('rust-binary-x86-64-unknown-linux-gnu@%s' % ver, when='@%s platform=cray target=x86_64:' % ver, type='build')
        depends_on('rust-binary-powerpc64le-unknown-linux-gnu@%s' % ver, when='@%s platform=linux target=ppc64le:' % ver, type='build')
        depends_on('rust-binary-powerpc64le-unknown-linux-gnu@%s' % ver, when='@%s platform=cray target=ppc64le:' % ver, type='build')
        depends_on('rust-binary-x86-64-apple-darwin@%s' % ver, when='@%s platform=darwin target=x86_64:' % ver, type='build')
