import scapy.all as scapy
import subprocess
import sys
import re
import socket

ip = socket.gethostbyname(socket.gethostname())

def scan(ip):
    arp_request = scapy.ARP(pdst=ip) #Creates a request with that IP
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #broadcast mac address
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #Lists that gave a response


    #Printing them out
    print("IP\t\t\tMAC Address\n----------------------------------------")
    for element in answered_list:
        try:
            print(element[1].psrc + "\t\t" + element[1].hwsrc)
        except:
            return 0


def main():
    global ip
    while ip[-1] != '.':
        ip = ip[:-1]
    scan(ip + "1/24")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        opt_ip = sys.argv[1]
    main()