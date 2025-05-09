import os
import sys
from colorama import init, Fore, Back, Style

init()

def print_header(text):
    print(f"\n{Fore.CYAN}{'='*80}")
    print(f"{Fore.CYAN}  {text}")
    print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}\n")

def print_tool(name, description):
    print(f"{Fore.GREEN}[+] {name}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{description}{Style.RESET_ALL}\n")

def print_command(cmd):
    print(f"{Fore.YELLOW}$ {cmd}{Style.RESET_ALL}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print_header("GUIDE DES OUTILS ESSENTIELS KALI LINUX")

    print_header("OUTILS DE BASE")
    
    print_tool("Nmap - Scanner de ports et vulnérabilités", 
        "Scanner réseau puissant pour l'énumération et la découverte de services")
    print("Usage:")
    print_command("nmap -sV -sC <ip_cible>     # Scan avec détection de version et scripts par défaut")
    print_command("nmap -p- <ip_cible>         # Scanner tous les ports")

    print_tool("Metasploit Framework - Tests de pénétration",
        "Framework complet pour l'exploitation de vulnérabilités")
    print("Usage:")
    print_command("msfconsole")
    print_command("msf> search <nom_exploit>")
    print_command("msf> use <exploit>")
    print_command("msf> show options")

    print_tool("Wireshark - Analyse de trafic réseau",
        "Analyseur de protocoles réseau pour capturer et examiner le trafic en temps réel")
    print("Usage:")
    print_command("wireshark")

    print_tool("John the Ripper - Craquage de mots de passe",
        "Outil de craquage de mots de passe rapide et flexible")
    print("Usage:")
    print_command("john --wordlist=/usr/share/wordlists/rockyou.txt <fichier_hash>")

    print_tool("Burp Suite - Test d'applications web",
        "Suite d'outils pour l'audit de sécurité d'applications web")
    print("Usage:") 
    print_command("burpsuite")

    print_tool("Hydra - Attaques par force brute",
        "Outil rapide pour tester plusieurs protocoles d'authentification")
    print("Usage:")
    print_command("hydra -l <utilisateur> -P <wordlist> <ip_cible> <service>")
    print_command("# Exemple: hydra -l admin -P /usr/share/wordlists/rockyou.txt 192.168.1.1 ssh")

    print_tool("Aircrack-ng - Audit de réseaux WiFi",
        "Suite d'outils pour tester la sécurité des réseaux sans fil")
    print("Usage:")
    print_command("airmon-ng start wlan0")
    print_command("airodump-ng wlan0mon")

    print_header("MAINTENANCE DU SYSTÈME")
    
    print("Mise à jour du système:")
    print_command("sudo apt update")
    print_command("sudo apt upgrade -y")
    
    print("\nInstallation d'outils:")
    print_command("sudo apt install <nom_outil>")
    
    print("\nMise à jour des bases de données:")
    print_command("sudo searchsploit -u  # Mettre à jour ExploitDB")
    print_command("sudo msfupdate       # Mettre à jour Metasploit")
    
    print("\nGestion des dépôts:")
    print_command("sudo nano /etc/apt/sources.list")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Programme interrompu par l'utilisateur{Style.RESET_ALL}")
        sys.exit(0)
