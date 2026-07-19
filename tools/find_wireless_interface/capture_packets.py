from scapy import *
from scapy.all import sniff
from scapy.layers.dot11 import Dot11, Dot11Elt
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.inet import ICMP


def capture_packets(interface):
    """
    Capture packets on the specified network interface.

    Args:
        interface (str): The name of the network interface to capture packets from.
        packet_count (int): The number of packets to capture.

    Returns:
        list: A list of captured packets.
    """
    
    result =sniff(iface= interface,  store=True , count = 10)

    for packet in result:

    # -------------------- Dot11 Layer --------------------
     if packet.haslayer(Dot11):
        print("[Dot11 Layer]")
        print(f"Source MAC      : {packet.addr2}")
        print(f"Destination MAC : {packet.addr1}")
        print(f"BSSID           : {packet.addr3}")
    
    # -------------------- Dot11Elt Layer --------------------
     if packet.haslayer(Dot11Elt):
        print("\n[Dot11Elt Layer]")
        ssid = packet[Dot11Elt].info.decode(errors='ignore')  # Decode SSID, ignoring errors
        print(f"source MAC      : {packet.addr2}")
        print(f"Destination MAC : {packet.addr1}")
        print(f"BSSID           : {packet.addr3}")
        print(f"SSID            : {ssid}")
        print(f"SSID Length     : {len(ssid)}")
        print(f"SSID Type       : {type(ssid)}")
        print(f"SSID Raw Bytes  : {packet[Dot11Elt].info}")
        print(f"SSID Raw Bytes Length: {len(packet[Dot11Elt].info)}")
        print(f"SSID Raw Bytes Type  : {type(packet[Dot11Elt].info)}")
        print(f"SSID Raw Bytes (Hex) : {packet[Dot11Elt].info.hex()}")
        print(f"SSID Raw Bytes (Hex Length): {len(packet[Dot11Elt].info.hex())}")
        print(f"SSID Raw Bytes (Hex Type)  : {type(packet[Dot11Elt].info.hex())}")
        print(f"SSID Raw Bytes (Hex Representation) : {packet[Dot11Elt].info.hex()}")
        print(f"SSID Raw Bytes (Hex Representation Length): {len(packet[Dot11Elt].info.hex())}")
        print(f"SSID Raw Bytes (Hex Representation Type)  : {type(packet[Dot11Elt].info.hex())}")
        print(f"SSID Raw Bytes (Hex Representation) : {packet[Dot11Elt].info.hex()}")
        print(f"SSID Raw Bytes (Hex Representation Length): {len(packet[Dot11Elt].info.hex())}")



    # -------------------- IP Layer -----------------------
     if packet.haslayer(IP):
        print("\n[IP Layer]")
        print(f"Source IP       : {packet[IP].src}")
        print(f"Destination IP  : {packet[IP].dst}")
        print(f"Protocol Number : {packet[IP].proto}")
        print(f"TTL             : {packet[IP].ttl}")
        print(f"Version         : {packet[IP].version}")
        print(f"Header Length   : {packet[IP].ihl * 4} bytes")
        print(f"summary        : {packet[IP].summary()}")

    # -------------------- TCP ----------------------------
     if packet.haslayer(TCP):
        print("\n[TCP]")
        print(f"Source Port     : {packet[TCP].sport}")
        print(f"Destination Port: {packet[TCP].dport}")

    # -------------------- UDP ----------------------------
     elif packet.haslayer(UDP):
        print("\n[UDP]")
        print(f"Source Port     : {packet[UDP].sport}")
        print(f"Destination Port: {packet[UDP].dport}")

    # -------------------- ICMP ---------------------------
     elif packet.haslayer(ICMP):
        print("\n[ICMP]")
        print(f"Type            : {packet[ICMP].type}")
        print(f"Code            : {packet[ICMP].code}")

    # -------------------- General Info -------------------
     print(f"\nPacket Length   : {len(packet)} bytes")
     print(f"Summary         : {packet.summary()}")
            
    
    
 
    



if __name__ == "__main__":
    interface = "Wi-Fi"  # Replace with your network interface
    capture_packets(interface)
