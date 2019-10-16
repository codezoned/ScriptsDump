"""
User Geo Location
=================

Get Geo location of user using https://ipstack.com/

written by: vimmrana0@gmail.com (vimm0)
original repository: https://github.com/vimm0/auto-script

USAGE:
=====
- Generate Free API key from https://ipstack.com/
- Obtain your ip address
- run the code

"""

import os
import requests
import re
import json


def check(Ip):
    # Make a regular expression
    # for validating an Ip-address
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
    # pass the regular expression
    # and the string in search() method
    if (re.search(regex, Ip)):
        return
    else:
        raise Exception('Invalid Ip address')


def screen_clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_geolocation_for_ip(ip_addr, access_key):
    url = f"http://api.ipstack.com/{ip_addr}?access_key={access_key}"
    response = requests.get(url)
    response.raise_for_status()
    formatted_json = json.dumps(response.json(), indent=4)
    print(formatted_json)


def get_user_input():
    ip_addr = input("Enter IP Address: ")
    access_key = input("Enter IP Stack Access Code: ")
    check(ip_addr)
    get_geolocation_for_ip(ip_addr, access_key)


def main():
    try:
        screen_clear()
        get_user_input()
    except KeyboardInterrupt:
        exit(1)


if __name__ == '__main__':
    main()
    exit(0)
