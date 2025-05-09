import hashlib
import itertools
import string
import time
from colorama import init, Fore, Style

def print_banner():
    banner = f"""
{Fore.RED}╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗    ║ 
║   ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗   ║
║   ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║   ║
║   ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║   ║
║   ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝   ║
║   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝    ║
║                                                                           ║
║                      Craquage de Mots de Passe                           ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)

def generate_hash(password, hash_type='md5'):
    """Génère un hash à partir d'un mot de passe."""
    if hash_type == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif hash_type == 'sha1':
        return hashlib.sha1(password.encode()).hexdigest()
    elif hash_type == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    else:
        raise ValueError("Type de hash non supporté")

def brute_force(target_hash, char_set=string.ascii_lowercase, max_length=8, hash_type='md5'):
    """Attaque par force brute."""
    start_time = time.time()
    attempts = 0
    
    print(f"{Fore.YELLOW}[*] Démarrage de l'attaque par force brute...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[+] Hash cible: {target_hash}{Style.RESET_ALL}")
    
    for length in range(1, max_length + 1):
        for guess in itertools.product(char_set, repeat=length):
            attempts += 1
            guess_str = ''.join(guess)
            guess_hash = generate_hash(guess_str, hash_type)
            
            if attempts % 100000 == 0:
                elapsed = time.time() - start_time
                print(f"{Fore.GREEN}[*] Tentatives: {attempts}, Temps écoulé: {elapsed:.2f}s{Style.RESET_ALL}")
            
            if guess_hash == target_hash:
                elapsed = time.time() - start_time
                print(f"\n{Fore.GREEN}[+] Mot de passe trouvé !{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[+] Mot de passe: {guess_str}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[+] Tentatives: {attempts}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[+] Temps: {elapsed:.2f} secondes{Style.RESET_ALL}")
                return guess_str
                
    print(f"\n{Fore.RED}[-] Mot de passe non trouvé après {attempts} tentatives{Style.RESET_ALL}")
    return None

def dictionary_attack(target_hash, wordlist_file, hash_type='md5'):
    """Attaque par dictionnaire."""
    start_time = time.time()
    attempts = 0
    
    print(f"{Fore.YELLOW}[*] Démarrage de l'attaque par dictionnaire...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[+] Hash cible: {target_hash}{Style.RESET_ALL}")
    
    try:
        with open(wordlist_file, 'r', encoding='latin-1') as f:
            for line in f:
                attempts += 1
                password = line.strip()
                guess_hash = generate_hash(password, hash_type)
                
                if attempts % 10000 == 0:
                    elapsed = time.time() - start_time
                    print(f"{Fore.GREEN}[*] Tentatives: {attempts}, Temps écoulé: {elapsed:.2f}s{Style.RESET_ALL}")
                
                if guess_hash == target_hash:
                    elapsed = time.time() - start_time
                    print(f"\n{Fore.GREEN}[+] Mot de passe trouvé !{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}[+] Mot de passe: {password}{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}[+] Tentatives: {attempts}{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}[+] Temps: {elapsed:.2f} secondes{Style.RESET_ALL}")
                    return password
                    
        print(f"\n{Fore.RED}[-] Mot de passe non trouvé après {attempts} tentatives{Style.RESET_ALL}")
        return None
        
    except FileNotFoundError:
        print(f"{Fore.RED}[-] Fichier dictionnaire non trouvé: {wordlist_file}{Style.RESET_ALL}")
        return None

def main():
    init()
    print_banner()
    
    print(f"{Fore.CYAN}Entrez le hash à cracker: {Style.RESET_ALL}")
    target_hash = input().strip()
    
    print(f"{Fore.YELLOW}[*] Test de l'attaque par force brute{Style.RESET_ALL}")
    brute_force(target_hash, string.ascii_lowercase + string.digits, 6)
    
    print(f"\n{Fore.YELLOW}[*] Test de l'attaque par dictionnaire{Style.RESET_ALL}")
    dictionary_attack(target_hash, "wordlist.txt")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[-] Programme interrompu par l'utilisateur{Style.RESET_ALL}")