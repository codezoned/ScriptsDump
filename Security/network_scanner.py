#! usr/bin/env python



# Programmer: Zeid Al-Ameedi
# Date 02/17/2019
# Details: Code that uses module netifaces to access and get back your mac/ip address if an interface is specified.
# Possible that a machine might have more than one address. Thus we loop through ni.interfaces() and access the AF_LINK/
# AF_INET method which is a list of dictionaries to grab all the neccessary addresses.
# THEN the ARP request/response begins on everything within the subnet


import scapy.all as scapy
import netifaces as ni 
import os
import sys
import optparse



def scan(ip):
        print("\nARP protocol begins.\n")
        arp_request = scapy.ARP(pdst = ip) #ARP request from my IP searching for our parameter IP
        ether_obj = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #broadcast destination ff:ff....:ff must be used
        # for all broadcasts that way it reaches all stations
        
        packet = ether_obj/arp_request  #Ethernet part to send the destination broadcast, arp part for all ip
        # / is used to append objects
        _dict = {}
        answered = scapy.srp(packet, timeout=2, verbose=False)[0] #Sends packet with our own customized ether part <ether_obj>

        for pckt in answered:
                _dict[pckt[1].psrc] = pckt[1].hwsrc
        
        for k in _dict.keys():
                print("IP Address: ", k)
                print("Mac Address: ", _dict[k])
                print("--------------------------------------------")   

def get_AllmacAddr():
    for i in ni.interfaces(): 
        addr = ni.ifaddresses(i)
        print(addr[ni.AF_LINK][0]['addr']) # Mac addresses on network

def get_AllipAddr():
    for i in ni.interfaces():
        try:
            ip = ni.ifaddresses(i)[ni.AF_INET][0]['addr']
            print(ip)
        except:
            print("That IP won't work.")

def getIP():
    ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
    return ip 

def getMac():
    mac = ni.ifaddresses(interface)[ni.AF_LINK][0]['addr']
    return mac

def main():
    global interface
    global target_IP

    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target_IP", help = "Give IP Address directly.")
    parser.add_option("-i", "--interface", dest="interface", help="Network interface to extract IP & mac addr")
    (options, par) = parser.parse_args()
    if not options.interface and not options.target_IP:
        print("[+] Mac Addresses \n")
        get_AllmacAddr()
        print("\n[+] IP Addresses \n")
        get_AllipAddr()
    elif options.target_IP:
            target_IP=options.target_IP
            scan(str(target_IP)+'/24')
    else:
        interface=options.interface
        print("\n[+] My IP Address \n")
        i = getIP()
        print(i)
        print("\n[+] My Mac Address \n")
        m = getMac()
        print(m)
        print("\n\n")
        scan(str(i)+'/24')


if __name__ == '__main__':
    main()



