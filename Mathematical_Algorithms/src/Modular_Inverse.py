"""
    Written By @nishantcoder97 - Nishant Nahata
    Modular Inverse
"""

def extended_euclidian(a, b):
    if a % b == 0:
        return 0, 1
    y, x = extended_euclidian(b, a % b)
    y = y - x * int(a / b)
    return x, y

"""
    Condition: Inverse exists only when a and mod are coprime
"""
def inverse(a, mod):
    '''
    param: int a
    param: int mod
    returns: int b: such that (a * b) % mod = 1, or we can say that b is modular inverse of a w.r.t mod
    '''
    x, _ = extended_euclidian(a, mod)
    if x < 0:
        x += mod
    return x


if __name__ == '__main__':
        #### Tests ###
    print(inverse(2, 1000000007))
    print(inverse(500000004, 1000000007))

    print(inverse(324, 1000000007))
    print(inverse(780864203, 1000000007))

    print(inverse(5, 9))
    print(inverse(2, 9))

    print(inverse(256, 495))
    print(inverse(466, 495))
