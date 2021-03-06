import sys
import socket
from scapy.all import *

'''
sr               : Send and receive packets at layer 3
sr1              : Send packets at layer 3 and return only the first answer
srp              : Send and receive packets at layer 2
srp1             : Send and receive packets at layer 2 and return only the first answer
send             : Send packets at layer 3
sendp            : Send packets at layer 2
'''
def discover_network_devices():
    local_devices = []
    ip_addr_range = sys.argv[1]
    arp_packet = ARP(pdst=ip_addr_range)
    broadcast_packet = Ether(dst="ff:ff:ff:ff:ff:ff")
    stack_packet = broadcast_packet/arp_packet

    response = srp(stack_packet, timeout=10)[0]
    for sent, recv in response:
        host = socket.gethostbyaddr(recv.psrc)
        hostname, _, _ = host
        local_devices.append({"IP": recv.psrc, "MAC": recv.hwsrc, "HOSTNAME": hostname})
    
    print("\n", " " * 3, "IP" + " " * 20 + "MAC" + " " * 20 + "HOSTNAME")
    for local in local_devices:
        print(local["IP"], " " * 5, local["MAC"], " " * 5, local["HOSTNAME"])

if __name__=='__main__':
    discover_network_devices()
