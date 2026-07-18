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
    results =sniff(iface= interface, prn = lambda p : print(p.summary()), store=True)
    return results
    
def clean_results(results):
    """
    Clean the captured packet results.

    Args:
        results (list): A list of captured packets.

    Returns:
        list: A cleaned list of packets.
    """
    
    cleaned_results = []
    for packet in results:
        if packet.haslayer(Dot11):
            cleaned_results.append(packet)
    return cleaned_results



if __name__ == "__main__":
    interface = "Wi-Fi"  # Replace with your network interface
    capture_packets(interface)
