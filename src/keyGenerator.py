from random import randrange
from src.millerRabin import generateLargePrime
from src.math import gcd, findModInverse


def generateKey(keySize=1024):
    # 1: get p and q, prime numbers
    print("Generating p and q...")
    p, q = generateLargePrime(keySize), generateLargePrime(keySize)

    # 2: get n, p * q
    n = p * q

    # 3: get e
    print("Generating e...")
    e = None

    # Validate e
    while e is None or gcd(e, (p - 1) * (q - 1)) != 1:
        # Get random values in valid range
        e = randrange(2 ** (keySize - 1), 2 ** (keySize))

    # 4: get d, modular inverse of e
    print("Calculating d...")
    d = findModInverse(e, (p - 1) * (q - 1))

    # 5: get keys
    print("Done")
    publicKey = (n, e)
    privateKey = (n, d)

    print("Public key:", publicKey)
    print("Private key:", privateKey)

    return (publicKey, privateKey)
