import sys

def score(text):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'\n"
    s = 0
    for i in text:
        if i in charset or i == ' ' or i == '\'':
            s+=1
    return s

def xor(s1, s2):
    res = ""
    for i in range(0, len(s1)):
        res += chr(ord(s1[i]) ^ ord(s2[i%len(s2)]))
    return res

def main():
    best = ""
    b = 0
    for i in range(1, 256):
        c = xor(sys.argv[1].decode('hex'), chr(i))
        print(c,i)
        if score(c) > b:
            b = score(c)
            best = c
    print("Plaintext: {}".format(best))