#!/usr/bin/env python3
"""Predictable PRNG — real mini-challenge (weak-prng)."""
import base64, hashlib, json, os, struct, sys, zlib, wave, io, math, random, re, textwrap
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", 'mersenne-seed')


def main():
    mat = fetch_material()
    with open("/challenge/flag.enc", "w") as fh:
        fh.write(mat.get("delivery_blob", ""))
    seed = sum(ord(c) for c in (CHALLENGE_KEY or "")) % 1000000
    rng = random.Random(seed)
    nums = [rng.getrandbits(32) for _ in range(10)]
    with open("/challenge/numbers.txt", "w") as fh:
        fh.write("\n".join(str(n) for n in nums) + "\n")
    key_bytes = (CHALLENGE_KEY or "").encode()
    keystream = bytes(rng.getrandbits(8) for _ in range(len(key_bytes)))
    masked = bytes(a ^ b for a, b in zip(key_bytes, keystream))
    with open("/challenge/key.enc", "w") as fh:
        fh.write(masked.hex() + "\n")
    with open("/challenge/seed.hint", "w") as fh:
        fh.write("seed < 1000000\n")
    print("Weak PRNG — brute seed from numbers.txt, predict keystream, XOR key.enc.")


if __name__ == "__main__":
    main()
