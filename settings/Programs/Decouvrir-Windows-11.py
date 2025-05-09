import tkinter as tk
from tkinter import ttk, scrolledtext
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import json
import subprocess

ACCENT_COLOR = "#0078D4"
DARK_MODE = "#202020"
DARKER_MODE = "#171717" 
LIGHT_MODE = "#FFFFFF"
GRAY = "#808080"

TUTORIALS = {
    "Premier démarrage": """
Bienvenue dans Windows 11 !

Voici les premières étapes à suivre lors du démarrage de Windows 11 :

1. Connexion à votre compte Microsoft
- Connectez-vous avec votre compte Microsoft existant
- Ou créez-en un nouveau si nécessaire
- Vous pouvez aussi utiliser un compte local

2. Configuration de Windows Hello
- Configurez la reconnaissance faciale
- Ou l'empreinte digitale si disponible
- Définissez un code PIN de secours

3. Paramètres de confidentialité
- Choisissez vos préférences de confidentialité
- Activez/désactivez la télémétrie
- Gérez les autorisations des applications

4. Mise en route
- Découvrez le nouveau menu Démarrer
- Explorez le Centre de notifications
- Familiarisez-vous avec la nouvelle interface
""",

    "Configuration initiale": """
Configuration recommandée pour Windows 11 :

1. Mises à jour système
- Lancez Windows Update
- Installez toutes les mises à jour disponibles
- Redémarrez si nécessaire

2. Pilotes
- Vérifiez que tous les pilotes sont à jour
- Utilisez le Gestionnaire de périphériques
- Installez les pilotes manquants

3. Applications essentielles
- Navigateur web
- Antivirus
- Suite bureautique
- Lecteur multimédia

4. Personnalisation
- Thème sombre/clair
- Fond d'écran
- Barre des tâches
- Menu Démarrer
""",

    "Mise à jour Windows": """
Guide complet des mises à jour Windows 11 :

1. Windows Update
- Ouvrez les Paramètres Windows
- Accédez à Windows Update
- Recherchez les mises à jour
- Installez les mises à jour disponibles

2. Paramètres de mise à jour
- Configurez les heures actives
- Gérez la bande passante
- Définissez les options de redémarrage
- Consultez l'historique des mises à jour

3. Résolution des problèmes
- Exécutez l'outil de dépannage
- Vérifiez l'espace disque
- Réinitialisez Windows Update
- Contactez le support Microsoft
""",

    "Paramètres de base": """
Configuration des paramètres essentiels :

1. Système
- Affichage et résolution
- Son et notifications
- Alimentation et batterie
- Stockage et mémoire

2. Périphériques
- Bluetooth et appareils
- Imprimantes et scanners
- Souris et pavé tactile
- Clavier et saisie

3. Réseau
- Wi-Fi et Ethernet
- Mode avion
- VPN
- Point d'accès mobile

4. Comptes
- Compte Microsoft
- Comptes locaux
- Options de connexion
- Synchronisation
""",

    "Personnalisation rapide": """
Personnalisez rapidement Windows 11 :

1. Apparence
- Mode sombre/clair
- Couleur d'accentuation
- Transparence des fenêtres
- Effets visuels

2. Barre des tâches
- Position des icônes
- Comportement
- Widgets
- Notifications

3. Menu Démarrer
- Applications épinglées
- Documents récents
- Recommandations
- Disposition

4. Bureau
- Fond d'écran
- Thème
- Icônes
- Gadgets
""",

    "Thèmes Windows": """
Personnalisation des thèmes Windows 11 :

1. Thèmes intégrés
- Thèmes Windows par défaut
- Collection Microsoft
- Thèmes saisonniers
- Thèmes personnalisés

2. Éléments personnalisables
- Arrière-plan
- Couleurs
- Sons
- Curseurs de souris

3. Mode sombre
- Activation/désactivation
- Applications compatibles
- Personnalisation
- Programmation

4. Création de thèmes
- Sauvegarde
- Modification
- Partage
- Installation
""",

    "Fonds d'écran": """
Guide des fonds d'écran Windows 11 :

1. Types de fonds d'écran
- Images statiques
- Diaporamas
- Fonds d'écran animés
- Fonds d'écran Spotlight

2. Sources
- Collection Windows
- Photos personnelles
- Sites web
- Applications tierces

3. Paramètres
- Résolution
- Ajustement
- Rotation
- Multi-écrans

4. Gestion
- Organisation
- Sauvegarde
- Synchronisation
- Optimisation
""",

    "Couleurs système": """
Personnalisation des couleurs Windows 11 :

1. Couleur d'accentuation
- Sélection automatique
- Couleurs personnalisées
- Intensité
- Application

2. Modes de couleur
- Mode clair
- Mode sombre
- Mode personnalisé
- Programmation

3. Éléments colorés
- Barre des tâches
- Menu Démarrer
- Bordures
- Applications

4. Accessibilité
- Contraste élevé
- Filtres de couleur
- Daltonisme
- Luminosité
""",

    "Police et icônes": """
Personnalisation des polices et icônes :

1. Polices système
- Installation
- Gestion
- Taille
- Style

2. Icônes bureau
- Affichage
- Organisation
- Taille
- Style

3. Icônes système
- Corbeille
- Ce PC
- Réseau
- Utilisateur

4. Personnalisation
- Pack d'icônes
- Création
- Modification
- Restauration
""",

    "Effets visuels": """
Configuration des effets visuels Windows 11 :

1. Animations
- Effets de transition
- Animations de fenêtre
- Effets de menu
- Animations système

2. Transparence
- Effets d'acrylic
- Flou d'arrière-plan
- Mica
- Paramètres

3. Performance
- Optimisation
- Ajustements
- Mode jeu
- Mode économie

4. Effets spéciaux
- Snap Layouts
- Widgets
- Effets 3D
- Personnalisation
""",

    "Windows Defender": """
Guide complet de Windows Defender :

1. Protection en temps réel
- Analyse antivirus
- Protection réseau
- Protection ransomware
- Contrôle d'applications

2. Pare-feu
- Règles entrantes
- Règles sortantes
- Profils réseau
- Configuration avancée

3. Performances
- Analyses planifiées
- Exclusions
- Rapports
- Optimisation

4. Sécurité supplémentaire
- SmartScreen
- Contrôle de compte
- Sécurité réseau
- Protection des données
""",

    "Pare-feu Windows": """
Configuration du pare-feu Windows :

1. Paramètres de base
- Activation/désactivation
- Profils réseau
- Règles prédéfinies
- Notifications

2. Règles avancées
- Applications autorisées
- Ports ouverts
- Protocoles
- Services

3. Sécurité
- Journalisation
- Surveillance
- Blocage
- Exceptions

4. Configuration réseau
- Domaine
- Privé
- Public
- Personnalisé
""",

    "Contrôle des comptes": """
Gestion du contrôle des comptes utilisateurs :

1. Niveaux de sécurité
- Maximum
- Par défaut
- Réduit
- Désactivé

2. Notifications
- Paramètres
- Fréquence
- Types
- Personnalisation

3. Permissions
- Applications
- Installation
- Modifications système
- Administration

4. Configuration avancée
- Stratégies
- Scripts
- Tâches
- Journaux
""",

    "Sauvegardes système": """
Guide des sauvegardes Windows 11 :

1. Types de sauvegarde
- Système
- Fichiers
- Paramètres
- Applications

2. Méthodes
- Historique des fichiers
- Points de restauration
- Image système
- OneDrive

3. Planification
- Automatique
- Manuelle
- Fréquence
- Rétention

4. Restauration
- Fichiers
- Système
- Applications
- Paramètres
""",

    "Cryptage BitLocker": """
Guide du chiffrement BitLocker :

1. Configuration
- Activation
- Méthodes de déverrouillage
- Sauvegarde
- Options avancées

2. Types de chiffrement
- Disque système
- Disques de données
- Lecteurs USB
- Partitions

3. Gestion
- Mots de passe
- Clés de récupération
- Certificats
- TPM

4. Sécurité
- Algorithmes
- Politiques
- Audit
- Récupération
""",

    "Bureaux virtuels": """
Utilisation des bureaux virtuels :

1. Création
- Nouveau bureau
- Organisation
- Nommage
- Personnalisation

2. Gestion
- Déplacement
- Copie
- Suppression
- Raccourcis

3. Applications
- Disposition
- Épinglage
- Paramètres
- Synchronisation

4. Navigation
- Raccourcis clavier
- Gestes tactiles
- Timeline
- Task View
""",

    "Gestionnaire des tâches": """
Guide du Gestionnaire des tâches :

1. Processus
- Surveillance
- Priorité
- Affinity
- Détails

2. Performance
- CPU
- Mémoire
- Disque
- Réseau

3. Démarrage
- Applications
- Services
- Optimisation
- Impact

4. Utilisateurs
- Sessions
- Ressources
- Permissions
- Déconnexion
""",

    "Raccourcis clavier": """
Guide des raccourcis Windows 11 :

1. Système
- Windows + Tab
- Alt + Tab
- Windows + L
- Ctrl + Alt + Suppr

2. Applications
- Alt + F4
- Windows + D
- Windows + E
- Windows + R

3. Fenêtres
- Windows + Flèches
- Windows + M
- Windows + Home
- Snap Layouts

4. Personnalisation
- Création
- Modification
- Désactivation
- Restauration
""",

    "Applications par défaut": """
Configuration des applications par défaut :

1. Types de fichiers
- Extensions
- Protocoles
- Applications
- Associations

2. Navigateur web
- Configuration
- Extensions
- Moteur de recherche
- Synchronisation

3. Applications système
- Email
- Musique
- Photos
- Vidéos

4. Applications tierces
- Installation
- Configuration
- Permissions
- Désinstallation
""",

    "Cloud et OneDrive": """
Utilisation de OneDrive :

1. Configuration
- Compte Microsoft
- Dossiers
- Synchronisation
- Sauvegarde

2. Stockage
- Fichiers à la demande
- Quota
- Nettoyage
- Partage

3. Sécurité
- Chiffrement
- Authentification
- Permissions
- Historique

4. Collaboration
- Partage
- Édition
- Commentaires
- Versions
""",

    "Résolution problèmes": """
Guide de dépannage Windows 11 :

1. Outils intégrés
- Dépanneur
- Vérification système
- Diagnostic mémoire
- Nettoyage disque

2. Problèmes courants
- Démarrage
- Performance
- Réseau
- Applications

3. Solutions
- Réparation
- Restauration
- Réinitialisation
- Support Microsoft

4. Prévention
- Maintenance
- Surveillance
- Sauvegardes
- Mises à jour
""",

    "Mode sans échec": """
Utilisation du mode sans échec :

1. Démarrage
- F8 au démarrage
- Paramètres Windows
- MSConfig
- Recovery

2. Options
- Minimal
- Réseau
- Invite de commandes
- Restauration

3. Dépannage
- Pilotes
- Services
- Applications
- Système

4. Sortie
- Redémarrage normal
- Sauvegarde
- Diagnostic
- Réparation
""",

    "Restauration système": """
Guide de la restauration système :

1. Points de restauration
- Création
- Automatique
- Manuel
- Gestion

2. Restauration
- Sélection point
- Vérification
- Confirmation
- Suivi

3. Protection
- Configuration
- Espace disque
- Exclusions
- Fréquence

4. Dépannage
- Erreurs
- Alternatives
- Récupération
- Support
""",

    "Nettoyage disque": """
Guide du nettoyage de disque :

1. Analyse
- Fichiers système
- Fichiers temporaires
- Cache
- Corbeille

2. Options
- Sélection fichiers
- Compression
- Défragmentation
- Optimisation

3. Automatisation
- Planification
- Scripts
- Tâches
- Rapports

4. Maintenance
- Vérification
- Réparation
- Optimisation
- Surveillance
""",

    "Outils diagnostic": """
Guide des outils de diagnostic :

1. Performances
- Moniteur ressources
- Analyseur performances
- Fiabilité système
- DirectX

2. Réseau
- Ping
- Tracert
- Ipconfig
- Netstat

3. Système
- MSInfo32
- Event Viewer
- DxDiag
- PowerShell

4. Matériel
- Gestionnaire périphériques
- Diagnostic mémoire
- Vérification disque
- Tests matériels
"""
}

class Windows11GuideApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Guide Windows 11")
        self.geometry("1280x800")
        self.configure(fg_color=DARK_MODE)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.menu_visible = False
        self.current_menu = None

        self.main_frame = ctk.CTkFrame(self, fg_color=DARK_MODE)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.header = ctk.CTkFrame(self.main_frame, fg_color=DARKER_MODE, height=100)
        self.header.pack(fill="x", padx=10, pady=(0,20))
        
        self.menu_button = ctk.CTkButton(
            self.header,
            text="☰ Menu",
            command=self.toggle_menu,
            fg_color=ACCENT_COLOR,
            hover_color="#005ea6",
            width=100
        )
        self.menu_button.pack(side="left", padx=20, pady=20)
        
        self.title_label = ctk.CTkLabel(
            self.header,
            text="Windows 11 - Guide Complet",
            font=("Segoe UI Variable", 32, "bold"),
            text_color=ACCENT_COLOR
        )
        self.title_label.pack(pady=20)

        self.content = ctk.CTkFrame(self.main_frame, fg_color=DARKER_MODE)
        self.content.pack(fill="both", expand=True, padx=10)

        self.menu_frame = ctk.CTkFrame(self.main_frame, fg_color=DARKER_MODE, width=300)
        
        self.menu_categories = {
            "Démarrage": [
                "Premier démarrage",
                "Configuration initiale", 
                "Mise à jour Windows",
                "Paramètres de base",
                "Personnalisation rapide"
            ],
            "Personnalisation": [
                "Thèmes Windows",
                "Fonds d'écran",
                "Couleurs système",
                "Police et icônes",
                "Effets visuels"
            ],
            "Sécurité": [
                "Windows Defender",
                "Pare-feu Windows",
                "Contrôle des comptes",
                "Sauvegardes système",
                "Cryptage BitLocker"
            ],
            "Productivité": [
                "Bureaux virtuels",
                "Gestionnaire des tâches",
                "Raccourcis clavier", 
                "Applications par défaut",
                "Cloud et OneDrive"
            ],
            "Dépannage": [
                "Résolution problèmes",
                "Mode sans échec",
                "Restauration système",
                "Nettoyage disque",
                "Outils diagnostic"
            ]
        }

    def toggle_menu(self):
        if self.menu_visible:
            self.menu_frame.pack_forget()
            self.menu_visible = False
        else:
            self.menu_frame.pack(side="left", fill="y", padx=10, pady=10)
            self.menu_visible = True
            self.create_menu()

    def create_menu(self):
        for widget in self.menu_frame.winfo_children():
            widget.destroy()

        for category, items in self.menu_categories.items():
            category_frame = ctk.CTkFrame(self.menu_frame, fg_color=DARK_MODE)
            category_frame.pack(fill="x", padx=5, pady=5)
            
            category_button = ctk.CTkButton(
                category_frame,
                text=category,
                command=lambda c=category: self.toggle_category(c),
                fg_color=ACCENT_COLOR,
                hover_color="#005ea6",
                width=280
            )
            category_button.pack(pady=2)
            
            items_frame = ctk.CTkFrame(category_frame, fg_color=DARKER_MODE)
            setattr(self, f"{category}_items", items_frame)
            
            for item in items:
                item_button = ctk.CTkButton(
                    items_frame,
                    text=f"• {item}",
                    command=lambda i=item: self.show_content(i),
                    fg_color="transparent",
                    hover_color=DARK_MODE,
                    anchor="w"
                )
                item_button.pack(fill="x", pady=1)

    def toggle_category(self, category):
        items_frame = getattr(self, f"{category}_items")
        if items_frame.winfo_manager():
            items_frame.pack_forget()
        else:
            items_frame.pack(fill="x", padx=5, pady=2)

    def show_content(self, content_type):
        for widget in self.content.winfo_children():
            widget.destroy()
            
        text = scrolledtext.ScrolledText(
            self.content,
            font=("Segoe UI Variable", 12),
            bg=DARKER_MODE,
            fg="white",
            relief="flat"
        )
        text.pack(fill="both", expand=True, padx=10, pady=10)
        
        if content_type in TUTORIALS:
            text.insert("1.0", TUTORIALS[content_type])
        else:
            text.insert("1.0", f"Le tutoriel pour {content_type} est en cours de rédaction...")
            
        text.configure(state="disabled")

if __name__ == "__main__":
    app = Windows11GuideApp()
    app.mainloop()