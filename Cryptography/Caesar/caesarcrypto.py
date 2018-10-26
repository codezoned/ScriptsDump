import string
alphabet=list(string.ascii_lowercase)
alphalen=len(alphabet)

def encrypt(input, key):
    plaintext = ''
    for x in input:
        if x is not ' ':
            plaintext += x
    ciphertext = ''
            
    for x in plaintext:
        if x in alphabet:
            step = (alphabet.index(x)+key)%alphalen
            ciphertext += alphabet[step]
        else:
            ciphertext += x
    return ciphertext


def decrypt(cipher, key):
    plaintext = ''
    for x in cipher:
        step = (alphabet.index(x)-key)%alphalen
        plaintext += alphabet[step]
    return plaintext

text = encrypt('my name is chef', 150)
text2 = decrypt(text, 150)
print ("%s \n%s" % (text, text2))
