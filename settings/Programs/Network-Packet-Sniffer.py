import sys
import scapy.all as scapy
from colorama import Fore, Style, init
from datetime import datetime

def analyze_packet(packet):
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst
        proto = packet[scapy.IP].proto

        if packet.haslayer(scapy.TCP):
            src_port = packet[scapy.TCP].sport
            dst_port = packet[scapy.TCP].dport
            print(f"{Fore.GREEN}TCP {src_ip}:{src_port} -> {dst_ip}:{dst_port}{Style.RESET_ALL}")
            
        elif packet.haslayer(scapy.UDP):
            src_port = packet[scapy.UDP].sport
            dst_port = packet[scapy.UDP].dport
            print(f"{Fore.BLUE}UDP {src_ip}:{src_port} -> {dst_ip}:{dst_port}{Style.RESET_ALL}")
            
        elif packet.haslayer(scapy.ICMP):
            print(f"{Fore.YELLOW}ICMP {src_ip} -> {dst_ip}{Style.RESET_ALL}")

def start_capture(interface=None):
    try:
        print(f"{Fore.CYAN}Démarrage de la capture sur {interface if interface else 'toutes les interfaces'}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Appuyez sur Ctrl+C pour arrêter{Style.RESET_ALL}\n")
        
        scapy.sniff(iface=interface, prn=analyze_packet, store=0)
        
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Capture arrêtée{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur: {str(e)}{Style.RESET_ALL}")

def main():
    init()
    
    if len(sys.argv) > 1:
        interface = sys.argv[1]
    else:
        interface = None
        
    start_capture(interface)

if __name__ == "__main__":
    main()
