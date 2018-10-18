from hashlib import md5

text = input('text:')
hash = md5(text.encode())

print('Original: %s' % (text))
print('Hash: %s' % (hash.hexdigest()))
