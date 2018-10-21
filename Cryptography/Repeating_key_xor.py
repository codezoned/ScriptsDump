import itertools
def repkey_xor(b,key):
    return b''.join([xor(chr(x).encode(),chr(y).encode()) for (x,y) in zip(b,itertools.cycle(key))])
    
text = "Sir Issac Newton formulated the laws of motion and universal gravitation"
key = "APPLE"
print(repkey_xor(text,key))
