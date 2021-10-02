from src.lowPrimes import lowPrimes
from random import randrange


def millerRabin(num):
    s = num - 1
    t = 0

    while s % 2 == 0:
        s = s // 2
        t += 1

    for _ in range(5):
        a = randrange(2, num - 1)
        v = pow(a, s, num)

        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num

        return True


def isPrime(num):
    # 2 is the first prime
    if num < 2:
        return False

    if num in lowPrimes:
        return True

    for prime in lowPrimes:
        if num % prime == 0:
            return False

    return millerRabin(num)


def generateLargePrime(keySize=1024):
    while True:
        num = randrange(2 ** (keySize - 1), 2 ** (keySize))
        if isPrime(num):
            return num
