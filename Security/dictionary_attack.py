import hashlib
import sys
import crypt

global g_hash 

def brute_force(hashstr, fi):
    temp = []
    counter = 0
    if '$6$' in hashstr:
        temp = hashstr.split('$')
        salt = temp[2]
        correct_hash = g_hash
        for guess in fi:
            counter += 1
            guess = guess.rstrip()
            result = crypt.crypt(guess, '$6$' + salt)
            if result == correct_hash:
                print("\n[{0}] Attempts.\n\n".format(counter))
                print("[+] Password found: {0}".format(guess))
                exit()
        print("[-] No password found.")
    else:
        print("SHA512 hashing algorithm was not used in this instance.")

def main():
    global g_hash
    if len(sys.argv) < 2:
        print("[-] Pass in dictionary file.")
    else:
        file_cracker = open(sys.argv[1], "r")
        g_hash = raw_input("[+] Input the hash [SHA512]: ")
        brute_force(g_hash, file_cracker)


if '__main__' == __name__:
    main()