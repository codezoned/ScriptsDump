import math


def round_complex(comp, prec=3):
    # rounding off the imaginary and real parts of the complex number.
    a, b = map(lambda x: round(x, prec), (comp.real, comp.imag))
    return complex(a, b) if b else a


def euler_pow(x):
    # returns: e ** (xj)
    return math.cos(x) + 1j * math.sin(x)


def fft(x, inv=False):
    n = len(x)
    if n == 1:
        return x
    w_n = euler_pow((-1 if inv else 1) * 2 * math.pi / n)
    w = 1
    y_0, y_1 = fft(x[0::2], inv), fft(x[1::2], inv)
    ans = [0 for i in range(n)]
    for k in range((n >> 1)):
        t = w * y_1[k]
        ans[k] = y_0[k] + t
        ans[k + (n >> 1)] = y_0[k] - t
        w = w * w_n
    return tuple(map(round_complex, ans))


def ifft(x):
    n = len(x)
    max_d = (n - 1).bit_length()
    return tuple(round_complex(comp / n) for comp in fft(x, inv=True))


if __name__ == '__main__':
    sequence = tuple(map(int, input("Enter the input Sequence: ").split()))
    op = fft(sequence)
    decoded = ifft(op)
    print("FFT sequence:", op)
    print("Decoded Sequence", decoded)


"""
Sample i/o:
Enter the input Sequence: 1  3 2 3 0 0 4 5
FFT sequence: (18, (4.536-1.293j), (-5-5j), (-2.536+2.707j), -4, (-2.536-2.707j), (-5+5j), (4.536+1.293j))
IFFT sequence: (1.0, 3.0, 2.0, 3.0, 0.0, -0.0, 4.0, 5.0)
"""

