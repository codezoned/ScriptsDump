import os
import random
import sys

# Checks if the key has the correct combination of ASCII values 
def bruteforce_key(key):
    chsum = 0
    for ch in key:
        chsum += ord(ch)
    sys.stdout.write("{0:3} | {1}   \r".format(chsum, key))
    sys.stdout.flush()
    return chsum

# Creates a key based on all possible characters used in a reasonable password 
def initializekey():
    key = ""
    inc = 0
    while True and inc <= 100:
        key += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_!@#$%^&*")
        ascii_code = bruteforce_key(key)
        if ascii_code > 916:
            key = ""
        elif ascii_code==916: 
            print("Password key: {0}\t{1}".format(key, inc))
            inc += 1

def main():
    initializekey()
    print("100 password options found.")

if __name__ == "__main__":
    main()


