def fence(lst, height):
    _fence = [[None] * len(lst) for n in range(height)]
    rails = [*range(0, height - 1), *range(height - 1, 0, -1)]  # sawtooth.
    for n, x in enumerate(lst): 
        _fence[rails[n % len(rails)]][n] = x
    return [c for c in sum(_fence, []) if c is not None]


def encode(text, h):
    return ''.join(fence(text, h))


def decode(cipher, h):
    pos = fence(range(len(cipher)), h)
    return ''.join(cipher[pos.index(i)] for i in range(len(cipher)))


if __name__ == '__main__':
    height = 3
    plain_text = "Hacktoberfest"
    cipher_text = encode(plain_text, height)
    decoded = decode(cipher_text, height)

    assert decoded == plain_text

