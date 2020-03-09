# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBootstrap(RustBootstrapPackage):
    """This package can bootstrap any version of the Rust compiler.

    Unlike the versioned rust-bootstrap packages (rust-bootstrap-1-*), this
    package does not provide the ability to bootstrap other versions of Rust.
    This is because it is not currently possible to have a package depend
    on itself in Spack. Therefore, you need a distinct package for each
    stage of the bootstrap, which is why the versioned packages exist.

    If you want to install a bootstrapped version of Rust, then you should
    install this package, and then specify the package dependency tree as
    necessary.
    """

    homepage = "https://www.rust-lang.org/"
    url      = "https://static.rust-lang.org/dist/rustc-1.41.0-src.tar.gz"

    maintainers = ['AndrewGaspar']

    # indicates that this is the ultimate target of a Rust bootstrapping build
    final_bootstrap = True

    variant(
        'mrustc',
        default=False, description='Prefer bootstrapping from mrustc')

    variant(
        'rustfmt',
        default=True,
        description='Formatting tool for Rust code'
    )

    variant(
        'analysis',
        default=True,
        description='Outputs code analysis that can be consumed by other tools'
    )

    variant(
        'clippy',
        default=True,
        description='Linting tool for Rust'
    )

    variant(
        'rls',
        default=False,
        description='The Rust Language Server can be used for IDE integration'
    )

    variant(
        'src',
        default=True,
        description='Install Rust source files'
    )

    releases = [
        ('1.41.1', '38c93d016e6d3e083aa15e8f65511d3b4983072c0218a529f5ee94dd1de84573'),
        ('1.41.0', '5546822c09944c4d847968e9b7b3d0e299f143f307c00fa40e84a99fabf8d74b'),
        ('1.40.0', 'dd97005578defc10a482bff3e4e728350d2099c60ffcf1f5e189540c39a549ad'),
        ('1.39.0', 'b4a1f6b6a93931f270691aba4fc85eee032fecda973e6b9c774cd06857609357'),
        ('1.38.0', '644263ca7c7106f8ee8fcde6bb16910d246b30668a74be20b8c7e0e9f4a52d80'),
        ('1.37.0', '120e7020d065499cc6b28759ff04153bfdc2ac9b5adeb252331a4eb87cbe38c3'),
        ('1.36.0', '04c4e4d7213d036d6aaed392841496d272146312c0290f728b7400fccd15bb1b'),
        ('1.35.0', '5a4d637a716bac18d085f44dd87ef48b32195f71b967d872d80280b38cff712d'),
        ('1.34.2', 'c69a4a85a1c464368597df8878cb9e1121aae93e215616d45ad7d23af3052f56'),
        ('1.34.1', 'b0c785264d17e1dac4598627c248a2d5e07dd39b6666d1881fcfc8e2cf4c40a7'),
        ('1.34.0', '7ac85acffd79dd3a7c44305d9eaabd1f1e7116e2e6e11e770e4bf5f92c0f1f59'),
        ('1.33.0', '5a01a8d7e65126f6079042831385e77485fa5c014bf217e9f3e4aff36a485d94'),
        ('1.32.0', '4c594c7712a0e7e8eae6526c464bf6ea1d82f77b4f61717c3fc28fb27ba2224a'),
        ('1.31.1', '91d2fc22f08d986adab7a54eb3a6a9b99e490f677d2d092e5b9e4e069c23686a'),
        ('1.30.1', '36a38902dbd9a3e1240d46ab0f2ca40d2fd07c2ab6508ed7970c6c4c036b5b29'),
        ('1.30.0', 'cd0ba83fcca55b64c0c9f23130fe731dfc1882b73ae21bef96be8f2362c108ee'),
        ('1.29.2', '5088e796aa2e47478cdf41e7243fc5443fafab0a7c70a11423e57c80c04167c9'),
        ('1.29.1', 'f1b0728b66ce6bce6d72bbe5ea9e3a24ea22a045665da2ed8fcdfad14f61a349'),
        ('1.29.0', 'a4eb34ffd47f76afe2abd813f398512d5a19ef00989d37306217c9c9ec2f61e9'),
        ('1.28.0', '1d5a81729c6f23a0a23b584dd249e35abe9c6f7569cee967cc42b1758ecd6486'),
        ('1.27.2', '9a818c50cdb7880abeaa68b3d97792711e6c64c1cdfb6efdc23f75b8ced0e15d'),
        ('1.27.1', '2133beb01ddc3aa09eebc769dd884533c6cfb08ce684f042497e097068d733d1'),
        ('1.27.0', '2cb9803f690349c9fd429564d909ddd4676c68dc48b670b8ddf797c2613e2d21'),
        ('1.26.2', 'fb9ecf304488c9b56600ab20cfd1937482057f7e5db7899fddb86e0774548700'),
        ('1.26.1', '70a7961bd8ec43b2c01e9896e90b0a06804a7fbe0a5c05acc7fd6fed19500df0'),
        ('1.26.0', '4fb09bc4e233b71dcbe08a37a3f38cabc32219745ec6a628b18a55a1232281dd'),
        ('1.25.0', 'eef63a0aeea5147930a366aee78cbde248bb6e5c6868801bdf34849152965d2d'),
        ('1.24.1', '3ea53d45e8d2e9a41afb3340cf54b9745f845b552d802d607707cf04450761ef'),
        ('1.24.0', 'bb8276f6044e877e447f29f566e4bbf820fa51fea2f912d59b73233ffd95639f'),
        ('1.23.0', '7464953871dcfdfa8afcc536916a686dd156a83339d8ec4d5cb4eb2fe146cb91'),
        ('1.22.1', '8b7a42bdd6eb205a8c533eb41b5c42389a88158d060aed1e0f461f68c1fd3fd3'),
        ('1.22.0', '0ac96fbc4fc4a616f8b0ad2f458f2af7e03c141271624cfb2be907b05cbe4a69'),
        ('1.21.0', '1707c142244b5bd909993559c6116c81987c1de21d6207c05d3ecbe5bba548fa'),
        ('1.20.0', '2aa4875ff4472c6e35262bbb9052cb2623da3dae6084a858cc59d36f33f18214'),
        ('1.19.0', '15231f5053fb72ad82be91f5abfd6aa60cb7898c5089e4f1ac5910a731090c51'),
        ('1.18.0', 'd2dc36e99b9e2269488b2bcddde43c234e6bde03edf70cba82a027ff49c36111'),
        ('1.17.0', '4baba3895b75f2492df6ce5a28a916307ecd1c088dc1fd02dbfa8a8e86174f87'),
        ('1.16.0', 'f966b31eb1cd9bd2df817c391a338eeb5b9253ae0a19bf8a11960c560f96e8b4'),
        ('1.15.1', '2e7daad418a830b45b977cd7ecf181b65f30f73df63ff36e124ea5fe5d1af327'),
        ('1.15.0', 'f655e4fac9c2abb93eb579e29c408e46052c0e74b7655cd222c63c6743457673'),
        ('1.14.0', 'c790edd2e915bd01bea46122af2942108479a2fda9a6f76d1094add520ac3b6b'),
        ('1.13.0', 'ecb84775ca977a5efec14d0cad19621a155bfcbbf46e8050d18721bb1e3e5084'),
        ('1.12.1', '97913ae4cb255618aaacd1a534b11f343634b040b32656250d09d8d9ec02d3dc'),
        ('1.12.0', 'ac5907d6fa96c19bd5901d8d99383fb8755127571ead3d4070cce9c1fb5f337a'),
        ('1.11.0', '3685034a78e70637bdfa3117619f759f2481002fd9abbc78cc0f737c9974de6a'),
        ('1.10.0', 'a4015aacf4f6d8a8239253c4da46e7abaa8584f8214d1828d2ff0a8f56176869'),
        ('1.9.0',  'b19b21193d7d36039debeaaa1f61cbf98787e0ce94bd85c5cbe2a59462d7cfcd'),
        ('1.8.0',  'af4466147e8d4db4de2a46e07494d2dc2d96313c5b37da34237f511c905f7449'),
        ('1.7.0',  '6df96059d87b718676d9cd879672e4e22418b6093396b4ccb5b5b66df37bf13a'),
        ('1.6.0',  '3002a4a00004b0727709abeefe1ab1b2731845e4dab74566f363861801bb3326'),
        ('1.5.0',  '641037af7b7b6cad0b231cc20671f8a314fbf2f40fc0901d0b877c39fc8da5a0'),
        ('1.4.0',  '1c0dfdce5c85d8098fcebb9adf1493847ab40c1dfaa8cc997af09b2ef0aa8211'),
        ('1.3.0',  'ea02d7bc9e7de5b8be3fe6b37ea9b2bd823f9a532c8e4c47d02f37f24ffa3126'),
        ('1.2.0',  'ea6eb983daf2a073df57186a58f0d4ce0e85c711bec13c627a8c85d51b6a6d78'),
        ('1.1.0',  'cb09f443b37ec1b81fe73c04eb413f9f656859cf7d00bc5088008cbc2a63fa8a'),
        ('1.0.0',  'c304cbd4f7b25d116b73c249f66bdb5c9da8645855ce195a41bda5077b995eba')
    ]

    for ver, hash in releases:
        version(ver, sha256=hash)
        current_ver = Version(ver)
        prev_minor_ver = \
            Version('{}.{}'.format(current_ver[0], current_ver[1] - 1))
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
        # rust-bootstrap does not itself provide the ability to bootstrap since
        # it would result in possible recursive dependencies. You must use
        # the rust-bootstrap-* packages, which each are unique packages
        # allowing a continuous bootstrap from a first mrustc or rust-binary
        # source to your target version
        depends_on(
            'rust-can-bootstrap-{}'.format(current_ver.up_to(2).dashed),
            when='@{}'.format(ver),
            type='build')

        if current_ver >= Version('1.31'):
            depends_on(
                'rust-bootstrap-{} +mrustc'
                .format(prev_minor_ver.up_to(2).dashed),
                when='+mrustc',
                type='build')
