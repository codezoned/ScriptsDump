import time

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def decrypt(cipher, key):
    plaintext = ''
    for x in cipher:
        step = alphabet.index(x)-key
        if step < 0:
            step += 26
        plaintext += alphabet[step]
    return plaintext

def releaseBrutus(cipher):
    for x in range(0,26):
        meme = decrypt(cipher, x)
        print "#%s\t%s" % (x, meme)

startTime = time.time()
releaseBrutus('pbqdphlvfkhi')
print "Finished the attack in %s seconds" % (round(time.time()-startTime, 5))