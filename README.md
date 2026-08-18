# Predictable PRNG (`weak-prng`)

**Category:** cryptography · **Difficulty:** medium · **Points:** 300

Tokens come from a seeded Mersenne Twister; predict the next one to get the key.

## Run it

```bash
docker build -t sparflag/weak-prng .
# `deca-ai start weak-prng` (or the web UI) prints the docker run line with your
# SPARFLAG_SERVER + SPARFLAG_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is XOR-encrypted then base64-encoded. Discover the challenge key, then invert XOR+base64.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
deca-ai submit weak-prng 'sparflag{...}'
```

## Hints

- Collect enough outputs to recover the generator state.
- Reconstruct the state, then predict the token that reveals the key.
