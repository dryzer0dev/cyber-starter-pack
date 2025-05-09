import tkinter as tk
from tkinter import ttk, scrolledtext
import customtkinter as ctk
from PIL import Image, ImageTk
import os
from colorama import Fore, Style
import time
import threading
import json
import subprocess

DARK_RED = "#8B0000"
DARKER_RED = "#640000"
BLACK = "#000000"
DARK_GRAY = "#1A1A1A"
LIGHT_GRAY = "#2D2D2D"

class WindowsGuideApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Guide Windows 10 - XiwA")
        self.geometry("1200x800")
        self.configure(fg_color=BLACK)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.main_container = ctk.CTkFrame(self, fg_color=BLACK)
        self.main_container.pack(fill="both", expand=True, padx=20, pady=20)

        self.banner_label = ctk.CTkLabel(
            self.main_container,
            text="Guide Windows 10",
            font=("Roboto", 36, "bold"),
            text_color=DARK_RED
        )
        self.banner_label.pack(pady=20)
        self.animate_banner()

        self.sections = {
            "Installation & Configuration": {
                "Installation propre de Windows 10": self.create_installation_guide,
                "Première configuration": lambda: self.show_message("Guide de configuration initiale en développement"),
                "Mise à jour et pilotes": self.create_update_guide,
                "Configuration du BIOS/UEFI": self.create_bios_guide
            },
            "Sécurité Avancée": {
                "Hardening Windows": self.create_hardening_guide,
                "Configuration du pare-feu": self.create_firewall_guide,
                "Antivirus et protection": self.create_antivirus_guide,
                "Sauvegardes et restauration": self.create_backup_guide
            },
            "Optimisation Système": {
                "Optimisation des performances": self.create_performance_guide,
                "Nettoyage et maintenance": self.create_cleanup_guide,
                "Services et processus": self.create_services_guide,
                "Registre Windows": self.create_registry_guide
            },
            "Confidentialité & Anonymat": {
                "Paramètres de confidentialité": self.create_privacy_guide,
                "Configuration VPN": self.create_vpn_guide,
                "Navigation sécurisée": self.create_browsing_guide,
                "Chiffrement des données": self.create_encryption_guide
            },
            "Outils Avancés": {
                "PowerShell et scripts": self.create_powershell_guide,
                "Outils d'administration": self.create_admin_tools_guide,
                "Virtualisation": self.create_virtualization_guide,
                "Ligne de commande": self.create_cmd_guide,
                "Ouvrir Terminal": self.open_terminal,
                "Autre Fonction": self.other_function,
            },
            "Options Avancés": {
                "PowerShell": self.open_powershell,
                "CMD": self.open_cmd,
            }
        }

        self.create_sidebar()

        self.content_frame = ctk.CTkFrame(self.main_container, fg_color=LIGHT_GRAY, corner_radius=15)
        self.content_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.progress = ctk.CTkProgressBar(self.main_container)
        self.progress.pack(fill="x", padx=20, pady=10)
        self.progress.set(0)

    def open_powershell(self):
        try:
            subprocess.Popen(["powershell.exe"], shell=True)
        except Exception as e:
            self.show_message(f"Erreur lors de l'ouverture de PowerShell : {e}")

    def open_cmd(self):
        try:
            subprocess.Popen("start cmd", shell=True)
        except Exception as e:
            self.show_message(f"Erreur CMD : {e}")

    def animate_banner(self):
        def animation():
            colors = [DARK_RED, DARKER_RED]
            index = 0
            while True:
                self.banner_label.configure(text_color=colors[index % len(colors)])
                index += 1
                time.sleep(1)
        threading.Thread(target=animation, daemon=True).start()

    def create_sidebar(self):
        sidebar = ctk.CTkFrame(self.main_container, fg_color=DARK_GRAY, corner_radius=15, width=250)
        sidebar.pack(side="left", fill="y", padx=10, pady=10)

        for section in self.sections:
            button = ctk.CTkButton(
                sidebar,
                text=section,
                fg_color=DARK_RED,
                hover_color=DARKER_RED,
                corner_radius=10,
                command=lambda s=section: self.show_subsections(s)
            )
            button.pack(pady=5, padx=10, fill="x")

    def show_subsections(self, section):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        for subsection, callback in self.sections[section].items():
            button = ctk.CTkButton(
                self.content_frame,
                text=subsection,
                fg_color=DARK_RED,
                hover_color=DARKER_RED,
                corner_radius=10,
                command=callback
            )
            button.pack(pady=5, padx=10, fill="x")

    def show_message(self, message):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        label = ctk.CTkLabel(self.content_frame, text=message, font=("Roboto", 14))
        label.pack(pady=20)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def create_installation_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)

        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Guide d'installation de Windows 10

        1. Préparation
        • Télécharger l'ISO officiel de Windows 10
        • Créer une clé USB bootable
        • Sauvegarder vos données importantes

        2. Installation
        • Démarrer sur la clé USB
        • Choisir la langue et le clavier
        • Sélectionner "Installation personnalisée"
        • Partitionner le disque dur

        3. Configuration initiale
        • Ne pas utiliser les paramètres express
        • Désactiver la télémétrie
        • Configurer un compte local

        4. Post-installation
        • Installer les pilotes essentiels
        • Configurer Windows Update
        • Installer les logiciels de base
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def create_update_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)

        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Guide des mises à jour et pilotes Windows 10

        1. Windows Update
        • Vérifier les mises à jour automatiquement
        • Configurer les heures actives
        • Gérer les mises à jour importantes
        • Mettre à jour manuellement si nécessaire

        2. Pilotes essentiels
        • Pilotes de la carte mère
        • Pilotes graphiques (NVIDIA/AMD/Intel)
        • Pilotes audio
        • Pilotes réseau
        • Pilotes de périphériques

        3. Outils de mise à jour
        • Windows Update Assistant
        • Media Creation Tool
        • Outils de mise à jour des fabricants
        • Gestionnaire de périphériques

        4. Bonnes pratiques
        • Créer un point de restauration avant les mises à jour majeures
        • Vérifier la compatibilité des pilotes
        • Sauvegarder les pilotes actuels
        • Tester la stabilité après les mises à jour
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def open_terminal(self):
        try:
            subprocess.Popen("start cmd", shell=True)
        except Exception as e:
            self.show_message(f"Erreur lors de l'ouverture du terminal : {e}")

    def other_function(self):
        self.show_message("Fonctionnalité en cours de développement")

    def create_bios_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)

        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Guide de configuration du BIOS/UEFI

        • Accéder au BIOS/UEFI : Appuyer sur la touche spécifique (F2, DEL, ESC, selon la marque) au démarrage
        • Naviguer avec le clavier ou la souris (selon le BIOS)
        • Activer ou désactiver le Secure Boot
        • Configurer l'ordre de démarrage
        • Activer la virtualisation (Intel VT-x ou AMD-V)
        • Enregistrer et quitter
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def create_hardening_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Hardening Windows 10

        • Désactiver les services non essentiels
        • Configurer les stratégies de sécurité locales
        • Activer Windows Defender
        • Utiliser Windows Firewall avancé
        • Appliquer les mises à jour de sécurité
        • Désactiver l'ActiveX et les macros
        • Utiliser des comptes avec privilèges limités
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def create_firewall_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Configuration du pare-feu Windows

        • Accéder au panneau de configuration du pare-feu
        • Activer le pare-feu pour tous les profils
        • Créer des règles entrantes et sortantes
        • Bloquer ou autoriser des applications spécifiques
        • Surveiller les activités du pare-feu
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def create_antivirus_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Antivirus et protection Windows

        • Vérifier que Windows Defender est activé
        • Mettre à jour régulièrement la base de données
        • Effectuer des analyses complètes périodiquement
        • Utiliser des outils complémentaires si nécessaire
        • Éviter les logiciels antivirus tiers non reconnus
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def create_backup_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Sauvegardes et restauration

        • Utiliser l'Historique des fichiers Windows
        • Créer des images système régulières
        • Sauvegarder les paramètres importants
        • Stocker les sauvegardes sur un support externe
        • Tester la restauration périodiquement
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def create_performance_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Optimisation des performances Windows

        • Désactiver les effets visuels inutiles
        • Gérer les programmes au démarrage
        • Défragmenter le disque dur
        • Nettoyer les fichiers temporaires
        • Mettre à jour les pilotes
        • Désactiver les services inutiles
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def create_cleanup_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Nettoyage et maintenance

        • Utiliser le Nettoyage de disque
        • Supprimer les fichiers temporaires
        • Désinstaller les programmes inutiles
        • Vérifier l'intégrité des disques
        • Mettre à jour Windows et pilotes
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def create_services_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Services et processus Windows

        • Gérer les services via services.msc
        • Désactiver les services non nécessaires
        • Surveiller l'utilisation des ressources
        • Automatiser avec des scripts si besoin
        • Vérifier la stabilité après modification
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def create_registry_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Édition du Registre Windows

        • Utiliser regedit pour modifier le registre
        • Sauvegarder le registre avant modifications
        • Rechercher des clés spécifiques
        • Modifier ou supprimer des valeurs
        • Attention : risque de stabilité
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def create_privacy_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Paramètres de confidentialité

        • Gérer les permissions des applications
        • Désactiver la télémétrie
        • Contrôler la publicité ciblée
        • Gérer les données de diagnostic
        • Limiter le suivi en ligne
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def create_vpn_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Configuration VPN

        • Accéder aux paramètres VPN dans Windows
        • Ajouter une nouvelle connexion VPN
        • Entrer les détails du serveur
        • Authentification et connexion
        • Vérifier la connectivité
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def create_browsing_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Navigation sécurisée

        • Utiliser des navigateurs respectueux de la vie privée
        • Activer la navigation privée
        • Bloquer les trackers
        • Utiliser des extensions de sécurité
        • Éviter les sites suspects
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def create_encryption_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Chiffrement des données

        • Activer BitLocker sur les disques
        • Utiliser le chiffrement de bout en bout
        • Gérer les clés de récupération
        • Sauvegarder les clés en sécurité
        • Vérifier l'intégrité du chiffrement
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def create_powershell_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        PowerShell et scripts

        • Utiliser PowerShell pour automatiser
        • Exécuter des scripts
        • Gérer les modules
        • Exemple : Obtenir la liste des processus
        • Sécurité : Exécuter en mode restreint ou avec politique adaptée
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def create_admin_tools_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Outils d'administration

        • Gestionnaire de périphériques
        • Gestion de l'ordinateur (compmgmt.msc)
        • Planificateur de tâches
        • Outils de diagnostic
        • Utilisation de Windows Admin Center
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def create_virtualization_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Virtualisation

        • Activer la virtualisation dans le BIOS/UEFI
        • Utiliser Hyper-V ou autres solutions
        • Créer et gérer des machines virtuelles
        • Utiliser des outils comme VirtualBox, VMware
        • Conseils pour la performance
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')

    def create_cmd_guide(self):
        self.clear_content()
        content = ctk.CTkFrame(self.content_frame, fg_color=LIGHT_GRAY, corner_radius=15)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget = scrolledtext.ScrolledText(
            content,
            wrap=tk.WORD,
            font=("Roboto", 12),
            bg=LIGHT_GRAY,
            fg="white",
            relief="flat"
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)

        guide_text = """
        Ligne de commande (CMD)

        • Utiliser l'invite de commandes
        • Exécuter des commandes de base
        • Scripts batch
        • Automatisation simple
        • Exemple : ipconfig, ping, netstat
        """
        text_widget.insert(tk.END, guide_text)
        text_widget.configure(state='disabled')


if __name__ == "__main__":
    app = WindowsGuideApp()
    app.mainloop()