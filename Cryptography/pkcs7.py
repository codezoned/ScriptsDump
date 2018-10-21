from Crypto.Cipher import AES

def pad_pkcs7(b,blocksize=AES.block_size):
    blen = len(b)
    if blen == blocksize:
        return b
    ch = blocksize - blen % blocksize
    return b + bytes([ch]*ch)
    
def unpad_pkcs7(b):
    padn = b[-1]
    for i in range(len(b)-1,len(b)-padn-1,-1):
        if b[i] != b[-1]:
            return b
    return b[:-padn]
