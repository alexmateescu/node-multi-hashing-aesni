{
    "targets": [
        {
            "target_name": "multihashing",
            "sources": [
                "multihashing.cc",
                "cryptonight.c",
                "cryptonight_light.c",
                "sha3/sph_keccak.c",
                "crypto/oaes_lib.c",
                "crypto/c_keccak.c",
                "crypto/c_groestl.c",
                "crypto/c_blake256.c",
                "crypto/c_jh.c",
                "crypto/c_skein.c",
                "crypto/hash.c",
                "crypto/aesb.c"
            ],
            "include_dirs": [
                "crypto",
                "<!(node -e \"require('nan')\")",
            ],
            "cflags_cc": [
                "-std=c++0x"
            ],
        }
    ]
}
