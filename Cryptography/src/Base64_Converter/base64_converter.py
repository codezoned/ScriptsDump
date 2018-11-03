import base64

string = input('Text: ').encode()

encoded = base64.b64encode(string)
decoded = base64.b64decode(string)

print('Original:', string)
print('Encoded:', encoded)
print('Decoded:', decoded)
