import os
import subprocess
from colorama import Fore, Style
import time

red = Fore.RED
white = Fore.WHITE
reset = Style.RESET_ALL

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    print(f"""{red}
██╗  ██╗██╗██╗    ██╗ █████╗ 
╚██╗██╔╝██║██║    ██║██╔══██╗
 ╚███╔╝ ██║██║ █╗ ██║███████║
 ██╔██╗ ██║██║███╗██║██╔══██║
██╔╝ ██╗██║╚███╔███╔╝██║  ██║
╚═╝  ╚═╝╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝
                                    {white}Version 0{reset}
                                    {red}XIWA OWNS YOU{reset}
""")

menus = {
    "1": {
        "title": "DECOUVERTE WINDOWS",
        "options": [
            "Decouvrir Windows 10",
            "Decouvrir Windows 11",
        ]
    },
    "2": {
        "title": "LINUX & KALI",
        "options": [
            "Installation Kali Linux VM",
            "Outils Kali Essentiels",
        ]
    },
    "3": {
        "title": "Basic Cyber Tools",
        "options": [
            "Network-Vulnerability-Scanner",
            "Network-Traffic-Analyzer", 
            "Password-Cracking-Tools",
            "Network-Packet-Sniffer",
            "Web-Security-Testing-Tools"
        ]
    }
}

def display_menu(menu_id):
    menu = menus[menu_id]
    print(f"\n{red}╭{'─' * 70}")
    print(f"{red}│ {white}{menu['title']}")
    print(f"{red}├{'─' * 70}")
    
    for i, option in enumerate(menu["options"], 1):
        if i == len(menu["options"]):
            print(f"{red}├─ {white}{i:02d} {red}│ {white}{option}")
        else:
            print(f"{red}├─ {white}{i:02d} {red}│ {white}{option}")
    
    print(f"{red}├─ {white}00 {red}│ {white}{'Retour'}")
    print(f"{red}└{'─' * 72}")

def main_loop():
    while True:
        banner()
        print(f"\n{red}╭{'─' * 50}")
        print(f"{red}│ {white}MENU PRINCIPAL")
        print(f"{red}├{'─' * 50}")
        for key, menu in menus.items():
            print(f"{red}├─ {white}{key} {red}│ {white}{menu['title']}")
        print(f"{red}└{'─' * 50}{reset}")

        menu_choice = input(f"\n{red}[{white}>{red}]{white} Choix du menu (1-7) : ").strip()
        if menu_choice not in menus:
            clear()
            continue

        while True:
            clear()
            banner()
            display_menu(menu_choice)
            
            max_options = len(menus[menu_choice]["options"])
            option_choice = input(f"\n{red}[{white}>{red}]{white} Choix de l'option (00-{max_options:02d}) : ").strip()
            
            if not option_choice.isdigit() or int(option_choice) not in range(0, max_options + 1):
                clear()
                continue

            if option_choice == "0":
                clear()
                break

            option_index = int(option_choice) - 1
            selected_option = menus[menu_choice]["options"][option_index].replace(" ", "-")
            script_path = f"settings/programs/{selected_option}.py"

            clear()
            banner()
            if os.path.exists(script_path):
                print(f"\n{red}[{white}*{red}]{white} Lancement de {selected_option}...")
                time.sleep(1)
                clear()
                subprocess.run(["python", script_path])
                input(f"\n{red}[{white}>{red}]{white} Appuyez sur Entrée pour continuer...")
                clear()
            else:
                print(f"\n{red}[{white}!{red}]{white} Erreur : Le module '{selected_option}' n'est pas installé !{reset}")
                time.sleep(2)
                clear()

main_loop()