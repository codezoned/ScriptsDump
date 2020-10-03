#! usr/bin/env python

# Programmer: Zeid Al-Ameedi
# Details: 
# Run as    python script.py -i [interface] -m [new mac address]
# Changes the mac address on desired network interface. Uses Regex
# to determine if successful by parsing ifconfig command

import subprocess
import optparse
import re

def main():
    global interface
    global new_mac

    parser = optparse.OptionParser() #initialize instance of that object
    parser.add_option("-i", "--interface", dest = "interface", help="Network Interface to change the Mac Address")
    parser.add_option("-m", "--mac", dest="new_mac", help = "Enter new mac address in form xx:xx:xx:xx:xx:xx")

    (options, args) = parser.parse_args()
    if not options.interface or not options.new_mac:
        print("Interface and new mac address must be given.")
    else:
        interface=options.interface
        new_mac=options.new_mac
        newMac()


def newMac():
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

    output = subprocess.check_output(["ifconfig", interface])
    matches = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)
    if(new_mac in matches.group()):
        print("[+] Mac Address successfully changed to {0}".format(new_mac))
    else:
        print("[-] Mac Address was not changed.")

if __name__ == '__main__':
    main()
