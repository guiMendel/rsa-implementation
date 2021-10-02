def gcd(a, b):
    """Finds the greatest common divisor for two integers a and b"""
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, mod):
    """Finds the inverse of a, mod mod"""

    # 1 must be the GCD between the 2
    if gcd(a, mod) != 1:
        return None

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, mod

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

    # Apply mod
    return u1 % mod
