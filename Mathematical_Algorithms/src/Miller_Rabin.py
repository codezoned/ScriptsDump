# Code by BH4

from random import randint


def modular_pow(base, exponent, modulus):
    """Return (base^exponent) % modulus"""
    base = base % modulus

    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result*base) % modulus
        base = (base*base) % modulus

        exponent = exponent//2
    return result


def miller_rabin(n, k):
    """Check the primality of n with the Miller Rabin primality.

    n is a positive integer.
    k is a positive integer that determines the accuracy of the test.
    The larger the value of k the more checks that are done.

    If the result is False then n is definitely composite.
    If the result is True then n is probably prime.
    """

    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0:
        return False

    # Write n-1 as (2^r)*d with d odd
    r = 0
    d = n-1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness Loop
    composite = 1
    for i in range(k):
        a = randint(2, n-2)
        x = modular_pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for j in range(r-1):
            composite = 1
            x = modular_pow(x, 2, n)
            if x == 1:
                return False
            if x == n-1:
                composite = 0
                break
        if composite == 1:
            return False
    return True


# Example of use
for i in range(2, 16):
    if miller_rabin(i, 5):
        print("{} is probably a prime number.".format(i))
    else:
        print("{} is definitely a composite number.".format(i))
