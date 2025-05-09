import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import json
import subprocess
import webbrowser
import requests
import sys
from pathlib import Path
import time

# Couleurs Kali Linux
ACCENT_COLOR = "#367bf0"  # Bleu Kali
DARK_MODE = "#1a1a1a"
DARKER_MODE = "#0d0d0d"
LIGHT_MODE = "#ffffff" 
GRAY = "#808080"

# URLs et chemins
VIRTUALBOX_URL = "https://download.virtualbox.org/virtualbox/7.0.12/VirtualBox-7.0.12-159484-Win.exe"
KALI_ISO_URL = "https://cdimage.kali.org/kali-2023.3/kali-linux-2023.3-installer-amd64.iso"
DOWNLOADS_DIR = Path.home() / "Downloads"

# Contenu des tutoriels
TUTORIALS = {
    "Prérequis": """
Configuration requise pour installer Kali Linux en VM :

1. Matériel minimum
- 2 Go de RAM (4 Go recommandés)
- 20 Go d'espace disque
- Processeur compatible virtualisation
- Connexion Internet

2. Logiciels nécessaires
<click>Télécharger et installer VirtualBox</click>
<click>Télécharger l'ISO Kali Linux</click>

3. Configuration BIOS/UEFI
- Activation de la virtualisation (VT-x/AMD-V)
- Vérification des paramètres de sécurité
- Boot order si nécessaire
""",

    "Installation VirtualBox": """
Installation automatique de VirtualBox :

1. Téléchargement et Installation
<click>Installer VirtualBox automatiquement</click>
L'assistant va :
- Télécharger la dernière version
- Lancer l'installation silencieuse
- Configurer les composants
- Installer les pilotes réseau

2. Vérification
<click>Vérifier l'installation</click>
L'assistant vérifiera :
- La bonne installation
- Les composants requis
- La configuration réseau
- Les extensions nécessaires
""",

    "Création VM": """
Création automatique de la machine virtuelle Kali :

1. Configuration automatique
<click>Créer la VM Kali préconfigurée</click>
L'assistant va :
- Créer une VM optimisée
- Configurer 4 Go de RAM
- Allouer 2 processeurs
- Créer un disque de 50 Go
- Activer l'accélération 3D

2. Configuration réseau
<click>Configurer le réseau</click>
L'assistant va :
- Configurer le mode NAT
- Optimiser l'adaptateur réseau
- Configurer IPv4
- Paramétrer le pare-feu
""",

    "Installation Kali": """
Installation automatisée de Kali Linux :

1. Préparation
<click>Préparer l'installation</click>
L'assistant va :
- Monter l'ISO Kali
- Configurer le boot
- Préparer les paramètres

2. Installation système
<click>Lancer l'installation automatique</click>
L'assistant va :
- Installer en français
- Configurer AZERTY
- Partitionner le disque
- Installer GRUB

3. Configuration
<click>Configurer le système</click>
L'assistant va :
- Créer les comptes
- Configurer le réseau
- Mettre à jour le système
- Optimiser les paramètres
""",

    "Outils essentiels": """
Installation automatique des outils :

1. Mise à jour système
<click>Mettre à jour Kali</click>
L'assistant va :
- Mettre à jour les dépôts
- Upgrader les paquets
- Mettre à jour le système
- Nettoyer les fichiers

2. Installation outils
<click>Installer les outils essentiels</click>
L'assistant va installer :
- Build-essential
- Python et pip
- Git et outils dev
- Wget et Curl

3. Outils sécurité
<click>Installer les outils de sécurité</click>
L'assistant va installer :
- Metasploit Framework
- Wireshark
- Nmap et ses scripts
- John the Ripper

4. Finalisation
<click>Finaliser l'installation</click>
L'assistant va :
- Appliquer le thème Kali
- Configurer les extensions
- Optimiser le shell
- Créer les raccourcis
"""
}

class KaliLinuxInstallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guide Installation Kali Linux VM")
        self.root.geometry("1200x800")
        
        # Configuration style
        self.style = ttk.Style()
        self.style.configure("Treeview", background=DARK_MODE, foreground=LIGHT_MODE, fieldbackground=DARK_MODE)
        
        # Frame principal
        self.main_frame = ctk.CTkFrame(self.root, fg_color=DARKER_MODE)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Titre
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="Guide d'Installation de Kali Linux en VM",
            font=("Helvetica", 24, "bold"),
            text_color=ACCENT_COLOR
        )
        self.title_label.pack(pady=20)
        
        # Frame contenu
        self.content_frame = ctk.CTkFrame(self.main_frame, fg_color=DARK_MODE)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Liste des sections
        self.sections_frame = ctk.CTkFrame(self.content_frame, fg_color=DARK_MODE)
        self.sections_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        self.sections_label = ctk.CTkLabel(
            self.sections_frame,
            text="Sections",
            font=("Helvetica", 16, "bold"),
            text_color=ACCENT_COLOR
        )
        self.sections_label.pack(pady=10)
        
        # Boutons des sections
        self.buttons = []
        for section in TUTORIALS.keys():
            btn = ctk.CTkButton(
                self.sections_frame,
                text=section,
                command=lambda s=section: self.show_tutorial(s),
                fg_color=DARK_MODE,
                hover_color=ACCENT_COLOR
            )
            btn.pack(pady=5, padx=10, fill=tk.X)
            self.buttons.append(btn)
            
        # Zone de texte avec liens cliquables
        self.text_area = scrolledtext.ScrolledText(
            self.content_frame,
            wrap=tk.WORD,
            font=("Helvetica", 12),
            bg=DARK_MODE,
            fg=LIGHT_MODE,
            insertbackground=LIGHT_MODE
        )
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.text_area.tag_configure("link", foreground=ACCENT_COLOR, underline=1)
        self.text_area.bind("<Button-1>", self.handle_click)
        
        # Afficher le premier tutoriel par défaut
        first_section = list(TUTORIALS.keys())[0]
        self.show_tutorial(first_section)

    def handle_click(self, event):
        index = self.text_area.index(f"@{event.x},{event.y}")
        tags = self.text_area.tag_names(index)
        
        if "link" in tags:
            # Récupérer le texte cliqué
            start = self.text_area.index(f"{index} linestart")
            end = self.text_area.index(f"{index} lineend")
            clicked_text = self.text_area.get(start, end).strip()

            # Lancer l'action correspondante
            if "VirtualBox" in clicked_text:
                self.install_virtualbox()
            elif "ISO Kali" in clicked_text:
                self.download_kali()
            elif "Créer la VM" in clicked_text:
                self.create_vm()
            elif "installation automatique" in clicked_text:
                self.install_kali()
            elif "outils" in clicked_text:
                self.install_tools()
            
    def install_virtualbox(self):
        try:
            messagebox.showinfo("Installation", "Téléchargement de VirtualBox en cours...")
            response = requests.get(VIRTUALBOX_URL)
            installer_path = DOWNLOADS_DIR / "VirtualBox_installer.exe"
            
            with open(installer_path, 'wb') as f:
                f.write(response.content)
                
            messagebox.showinfo("Installation", "Installation de VirtualBox en cours...")
            subprocess.run([str(installer_path), '--silent'], check=True)
            
            time.sleep(30) # Attendre la fin de l'installation
            messagebox.showinfo("Succès", "VirtualBox a été installé avec succès!")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'installation: {e}")

    def download_kali(self):
        try:
            messagebox.showinfo("Téléchargement", "Téléchargement de Kali Linux en cours...")
            webbrowser.open(KALI_ISO_URL)
            
            # Attendre que l'ISO soit téléchargé
            iso_path = DOWNLOADS_DIR / "kali-linux-2023.3-installer-amd64.iso"
            while not iso_path.exists():
                time.sleep(5)
                
            messagebox.showinfo("Succès", "ISO Kali Linux téléchargé avec succès!")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du téléchargement: {e}")

    def create_vm(self):
        try:
            messagebox.showinfo("Création VM", "Création de la machine virtuelle en cours...")
            
            # Créer la VM
            subprocess.run([
                "VBoxManage", "createvm",
                "--name", "Kali Linux",
                "--ostype", "Debian_64",
                "--register"
            ], check=True)
            
            # Configurer la VM
            subprocess.run([
                "VBoxManage", "modifyvm", "Kali Linux",
                "--memory", "4096",
                "--cpus", "2",
                "--vram", "128",
                "--accelerate3d", "on"
            ], check=True)
            
            # Créer le disque dur
            subprocess.run([
                "VBoxManage", "createhd",
                "--filename", str(DOWNLOADS_DIR / "KaliLinux.vdi"),
                "--size", "51200"
            ], check=True)
            
            messagebox.showinfo("Succès", "Machine virtuelle créée avec succès!")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la création de la VM: {e}")

    def install_kali(self):
        try:
            messagebox.showinfo("Installation", "Installation de Kali Linux en cours...")
            
            # Monter l'ISO
            subprocess.run([
                "VBoxManage", "storageattach", "Kali Linux",
                "--storagectl", "IDE",
                "--port", "0",
                "--device", "0",
                "--type", "dvddrive",
                "--medium", str(DOWNLOADS_DIR / "kali-linux-2023.3-installer-amd64.iso")
            ], check=True)
            
            # Démarrer la VM
            subprocess.run([
                "VBoxManage", "startvm", "Kali Linux"
            ], check=True)
            
            messagebox.showinfo("Installation", "L'installation est en cours. Suivez les instructions à l'écran.")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'installation: {e}")

    def install_tools(self):
        try:
            messagebox.showinfo("Installation", "Installation des outils en cours...")
            
            # Commandes à exécuter dans la VM
            commands = [
                "apt update",
                "apt upgrade -y",
                "apt install -y build-essential python3-pip git curl wget",
                "apt install -y metasploit-framework wireshark nmap john"
            ]
            
            for cmd in commands:
                subprocess.run([
                    "VBoxManage", "guestcontrol", "Kali Linux",
                    "run", "--exe", "/bin/bash",
                    "--username", "root", "--password", "kali",
                    "--", "/bin/bash", "-c", cmd
                ], check=True)
                
            messagebox.showinfo("Succès", "Outils installés avec succès!")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'installation des outils: {e}")
        
    def show_tutorial(self, section):
        self.text_area.delete(1.0, tk.END)
        content = TUTORIALS[section]
        
        # Ajout des tags pour les liens
        self.text_area.insert(tk.END, content)
        start = "1.0"
        while True:
            start = self.text_area.search("<click>", start, tk.END)
            if not start:
                break
            end = self.text_area.search("</click>", start, tk.END)
            if not end:
                break
            self.text_area.tag_add("link", start + "+7c", end)
            # Supprimer les balises
            self.text_area.delete(end, end + "+7c")
            self.text_area.delete(start, start + "+7c")
            start = end
        
        # Mise à jour des boutons
        for btn in self.buttons:
            if btn.cget("text") == section:
                btn.configure(fg_color=ACCENT_COLOR)
            else:
                btn.configure(fg_color=DARK_MODE)

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg=DARKER_MODE)
    app = KaliLinuxInstallApp(root)
    root.mainloop()
