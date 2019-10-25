import sys
import hashlib
import requests


def check_password_occurrences(pwd):
    hashed = hashlib.sha1(pwd.encode('UTF-8')).hexdigest().upper()
    prefix = hashed[:5]
    print('SHA1 Hash:', hashed)

    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    print(f'URL: {url}')

    session = requests.Session()
    resp = session.get(f'{url}')
    status = resp.status_code
    print(f'Status: {status}')

    if status != 200:
        print('Error with the api service!')
        print(f'Received HTTP {status}')
        sys.exit()

    found = 0
    hashes = resp.content.decode('UTF-8')
    for h in hashes.split('\r\n'):
        check_hash = h[:35]
        if hashed[5:] == check_hash:
            found = int(h[36:])

    return found


def main():
    if len(sys.argv) <= 1:
        print('Usage: python pwd_checker.py <password>')

    pwd = sys.argv[1]
    print(f'Checking password: {pwd}')
    found = check_password_occurrences(pwd)

    if found:
        print('Found', found, 'occurrences of that password!')
    else:
        print('Password not found!')


if __name__ == '__main__':
    main()
