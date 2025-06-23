from scapy.all import sniff, IP, TCP, UDP

def show_packet(packet):
    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        proto = ""
        if packet.haslayer(TCP):
            proto = "TCP"
        elif packet.haslayer(UDP):
            proto = "UDP"
        else:
            proto = "Other"

        print(f"{src} --> {dst} | Protocol: {proto}")

print("Sniffing 10 packets...")
sniff(count=10, prn=show_packet)