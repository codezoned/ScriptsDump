import zipfile
import sys
from threading import thread

def extractFile(zfile, hash_dict):
    try:
        zfile.extractall(pwd=password)
        print("[+] Password found: {0}".format(password))
        exit()
    except RuntimeError:
        return

def main():
    if len(sys.argv < 2):
        print("[-] Pass zipfile and dictionary")
    else:
        zfile = zipfile.ZipFile(sys.argv[1], "r")
        hash_dict = open(sys.argv[2], 'r')
        for password in hash_dict:
            password = word.strip('\n')
            t = thread(target=extractFile, args=(zfile, password))        extractFile(zfile, hash_dict)
        print("[-] Incorrect password list")


if __name__ == '__main__':
    main()