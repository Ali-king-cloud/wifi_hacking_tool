from scapy import all
from scapy.all import sniff
from scapy.layers.dot11 import Dot11, Dot11Elt
from prettytable import PrettyTable
import os

def capture_packets(interface):
    """
    Capture packets on the specified network interface.

    Args:
        interface (str): The name of the network interface to capture packets from.
        packet_count (int): The number of packets to capture.

    Returns:
        list: A list of captured packets.
    """
    results = []
    # Start capturing packets on the specified interface
    sniff(iface= interface, prn = lambda p : print(p.summary()), store=True)
    
 
    



if __name__ == "__main__":
    interface = "Wi-Fi"  # Replace with your network interface
    capture_packets(interface)
