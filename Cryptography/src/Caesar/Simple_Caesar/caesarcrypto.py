alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(input, key):
    plaintext = ''
    for x in input:
        if x is not ' ':
            plaintext += x
    ciphertext = ''
    for x in plaintext:
        if x in alphabet:
            step = alphabet.index(x)+key
            if step > 25:
                step -= 26
            ciphertext += alphabet[step]
        else:
            ciphertext += x
    return ciphertext


def decrypt(cipher, key):
    plaintext = ''
    for x in cipher:
        step = alphabet.index(x)-key
        if step < 0:
            step += 26
        plaintext += alphabet[step]
    return plaintext

text = encrypt('my name is chef', 3)
text2 = decrypt(text, 3)
print "%s \n%s" % (text, text2)
