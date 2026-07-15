from scapy.all import rdpcap
from scapy.layers.inet import IP, ICMP, UDP
from scapy.packet import Raw
from scapy.layers.l2 import Ether
from scapy.sendrecv import srp
from scapy.sendrecv import sniff
from scapy import *
pkt = IP(dst="google.com")/ICMP()

pkt.show()
#now a taks:
udp_packet = Ether()/IP(dst="192.168.1.1")/UDP(dport=53)/Raw(load="Hello,scapy, this is a test UDP packet")
udp_packet.show()

answered, unanswered = srp(udp_packet, timeout = 2, verbose=True)
answered.summary()
unanswered.summary()
#Now we capture packets using sniffing
packets = sniff(count =10)
packets.summary()

