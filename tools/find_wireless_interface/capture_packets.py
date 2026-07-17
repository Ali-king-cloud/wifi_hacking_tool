from scapy import all
from scapy.all import sniff
from scapy.layers.dot11 import Dot11, Dot11Elt
def capture_packets(interface):
    """
    Capture packets on the specified network interface.

    Args:
        interface (str): The name of the network interface to capture packets from.
        packet_count (int): The number of packets to capture.

    Returns:
        list: A list of captured packets.
    """
    # Start capturing packets on the specified interface
    sniff(iface=interface, prn=packet_callback, store=False)
def packet_callback(packet):
    """
    Callback function to process each captured packet.

    Args:
        packet: The captured packet.
    """
    # Print the summary of the captured packet

    if packet.haslayer(Dot11):
        if packet.type == 0 and packet.subtype == 8:  # Beacon frame
            ssid = packet[Dot11Elt].info.decode()
            print(f"SSID: {ssid}")
        elif packet.type == 0 and packet.subtype == 4:  # Probe Response frame
            ssid = packet[Dot11Elt].info.decode()
            print(f"SSID: {ssid}")
    print(packet.summary())

if __name__ == "__main__":
    interface = "Wi-Fi"  # Replace with your network interface
    capture_packets(interface)