# --- ÉLÉMENTS DE PORTABILITÉ EN PYTHON ---

# Python est conçu pour être portable, mais certaines spécificités des systèmes
# d'exploitation peuvent affecter le fonctionnement du code. Voici comment
# écrire du code Python portable.

import os
import platform
import sys
from pathlib import Path


# --- Détection de la Plateforme ---

# `os.name` : Identifie le type de système
# - "posix" pour Linux/Mac
# - "nt" pour Windows

print("Système OS :", os.name)

# `platform.system()` : Nom précis du système d'exploitation
# - "Windows", "Linux", "Darwin" (macOS)

print("Plateforme :", platform.system())
print("Version :", platform.version())


# --- Gestion des Chemins Portables ---

# Sur différents systèmes, les chemins de fichiers diffèrent :
# - Windows utilise `\` comme séparateur de chemins.
# - Linux/macOS utilisent `/`.

# Utilisation de `os.path` pour manipuler les chemins :
chemin_absolu = os.path.abspath("fichier.txt")
print("Chemin absolu :", chemin_absolu)

# Utilisation de `os.path.join` pour construire des chemins portables :
chemin_portable = os.path.join("dossier", "sous_dossier", "fichier.txt")
print("Chemin portable :", chemin_portable)

# Utilisation de `Path` (module pathlib) pour la portabilité moderne :
chemin_pathlib = Path("dossier") / "sous_dossier" / "fichier.txt"
print("Chemin avec pathlib :", chemin_pathlib)


# --- Détection et Gestion des End-of-Line (EOL) ---

# Les différents systèmes utilisent différents caractères pour la fin de ligne :
# - "\n" sur Linux/macOS
# - "\r\n" sur Windows

# Exemple de lecture et écriture compatible :
contenu = "Ligne 1\nLigne 2\nLigne 3"

with open("fichier_eol.txt", "w", newline="") as fichier:
    fichier.write(contenu)

print("Fichier écrit avec des fins de ligne compatibles.")


# --- Commandes Spécifiques au Système ---

# Certaines commandes système sont spécifiques :
if os.name == "nt":  # Windows
    print("Commande système Windows :")
    os.system("dir")  # Affiche les fichiers du répertoire
else:  # Linux/macOS
    print("Commande système Linux/macOS :")
    os.system("ls")  # Affiche les fichiers du répertoire


# --- Gestion des Encodages ---

# Différents systèmes d'exploitation utilisent des encodages différents par défaut.
# Pour garantir la portabilité, utilisez UTF-8.

texte = "Bonjour, monde !"

# Écriture d'un fichier avec encodage UTF-8
with open("texte_portable.txt", "w", encoding="utf-8") as fichier:
    fichier.write(texte)

# Lecture d'un fichier avec encodage UTF-8
with open("texte_portable.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()
    print("Contenu du fichier :", contenu)


# --- Détection de l'Architecture ---

# Identifier si le système est 32 bits ou 64 bits
architecture = platform.architecture()
print("Architecture :", architecture)


# --- Variables d'Environnement ---

# Les variables d'environnement diffèrent entre les systèmes.
# Exemple : Obtenir la variable PATH.

print("Variable PATH :", os.getenv("PATH"))

# Définir une nouvelle variable d'environnement
os.environ["NOUVELLE_VAR"] = "Valeur"
print("Nouvelle variable d'environnement :", os.getenv("NOUVELLE_VAR"))


# --- Exécution de Programmes Externes ---

# Utilisation de `subprocess` pour une exécution portable
import subprocess

try:
    if os.name == "nt":
        resultat = subprocess.run(["echo", "Hello depuis Windows"], capture_output=True, text=True)
    else:
        resultat = subprocess.run(["echo", "Hello depuis Linux/macOS"], capture_output=True, text=True)
    print("Résultat de la commande :", resultat.stdout.strip())
except FileNotFoundError as e:
    print("Erreur :", e)


# --- Bibliothèques Standard Portables ---

# Utilisez toujours des bibliothèques Python standard lorsque cela est possible.
# Exemple : manipulation de fichiers, réseaux, gestion des threads.

import shutil

# Copie de fichiers portable
source = "texte_portable.txt"
destination = os.path.join("copie", "texte_portable.txt")

# Création d'un répertoire de destination
Path("copie").mkdir(exist_ok=True)

# Copie du fichier
shutil.copy(source, destination)
print(f"Fichier copié de {source} vers {destination}")


# --- Recommandations pour Écrire du Code Portable ---
# 1. Utilisez les modules standard (`os`, `pathlib`, `platform`, `shutil`).
# 2. Préférez les chemins relatifs ou dynamiques.
# 3. Gérez les différences d'encodage en utilisant UTF-8.
# 4. Testez votre code sur plusieurs systèmes d'exploitation.
