from scapy.all import sniff, IP, TCP

# Define allowed IPs and blocked ports
ALLOWED_IPS = ['192.168.1.1', '192.168.1.2']
BLOCKED_PORTS = [80, 443]

# Callback function to process each packet
def packet_callback(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        if ip_src not in ALLOWED_IPS:
            print(f"Blocked packet from {ip_src}")
            return
    if packet.haslayer(TCP):
        port = packet[TCP].dport
        if port in BLOCKED_PORTS:
            print(f"Blocked packet to port {port}")
            return
    print(packet.show())

# Start sniffing packets
sniff(prn=packet_callback, store=0)
