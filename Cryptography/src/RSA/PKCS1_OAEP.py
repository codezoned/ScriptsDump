# using pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
# You can use PKCS1_v1_5 mode just by replaceing PKCS1_OAEP with PKCS1_v1_5
import base64

# RSA involves a public key and private key.
# It is used to encrypt messages.
# The public key can be known to everyone; and
# messages encrypted using the public key can
# only be decrypted with the private key.


def do_encrypt(string_to_encrypt):
    bytes_to_encrypt = string_to_encrypt.encode("utf-8")
    key = RSA.import_key(open("public.pem").read())
    signer = PKCS1_OAEP.new(key)
    signed_data = signer.encrypt(bytes_to_encrypt)
    return base64.b64encode(signed_data).decode()


def do_decrypt(string_to_decrypt):
    key = RSA.import_key(open("private.pem").read())
    signer = PKCS1_OAEP.new(key)
    bytes_to_decrypt = base64.b64decode(string_to_decrypt.encode())
    unsigned_data = signer.decrypt(bytes_to_decrypt)
    return unsigned_data.decode("utf-8")


if __name__ == "__main__":
    test_string = "test_Test_test"
    print("Plain text:\t", test_string)
    encrypted_data = do_encrypt(test_string)
    print("Data after encryption:\t", encrypted_data)
    decrypted_data = do_decrypt(encrypted_data)
    print("Data after decryption:\t", decrypted_data)
