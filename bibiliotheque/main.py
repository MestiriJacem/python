# --- INTRODUCTION AUX BIBLIOTHÈQUES EN PYTHON ---

# Une bibliothèque est un ensemble de modules et de packages prêts à l'emploi.
# Python dispose de nombreuses bibliothèques intégrées (standard library),
# ainsi que des bibliothèques externes disponibles via PyPI (Python Package Index).

# --- Bibliothèques Standard ---

# 1. Bibliothèque `math` : opérations mathématiques avancées
import math

print("Pi :", math.pi)
print("Carré de 16 :", math.sqrt(16))
print("Cosinus de 45 degrés :", math.cos(math.radians(45)))


# 2. Bibliothèque `random` : génération de nombres aléatoires
import random

print("Nombre aléatoire entre 1 et 10 :", random.randint(1, 10))
print("Choix aléatoire dans une liste :", random.choice(["pierre", "papier", "ciseaux"]))


# 3. Bibliothèque `datetime` : gestion des dates et heures
from datetime import datetime

now = datetime.now()
print("Date et heure actuelles :", now)
print("Année :", now.year, "Mois :", now.month, "Jour :", now.day)


# 4. Bibliothèque `os` : interaction avec le système d'exploitation
import os

print("Répertoire de travail actuel :", os.getcwd())
print("Liste des fichiers dans le répertoire :", os.listdir("."))


# --- Bibliothèques Externes ---

# Pour utiliser une bibliothèque externe, il faut d'abord l'installer avec pip.
# Exemple : `pip install numpy pandas matplotlib`

# 1. Bibliothèque `numpy` : calcul scientifique
import numpy as np

# Création d'un tableau numpy
array = np.array([1, 2, 3, 4])
print("Tableau numpy :", array)
print("Somme des éléments :", np.sum(array))
print("Moyenne :", np.mean(array))


# 2. Bibliothèque `pandas` : manipulation et analyse des données
import pandas as pd

# Création d'un DataFrame
data = {"Nom": ["Alice", "Bob", "Claire"], "Age": [25, 30, 35]}
df = pd.DataFrame(data)
print("DataFrame pandas :\n", df)

# Lecture et écriture de fichiers CSV
df.to_csv("personnes.csv", index=False)
print("Lecture du fichier CSV :\n", pd.read_csv("personnes.csv"))


# 3. Bibliothèque `matplotlib` : visualisation de données
import matplotlib.pyplot as plt

# Tracer un graphique simple
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y, label="Ligne 1")
plt.title("Exemple de graphique")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()


# 4. Bibliothèque `requests` : interaction avec des APIs
import requests




# --- Gestion des Bibliothèques ---
# Installer une bibliothèque : `pip install nom_bibliotheque`
# Mettre à jour une bibliothèque : `pip install --upgrade nom_bibliotheque`
# Désinstaller une bibliothèque : `pip uninstall nom_bibliotheque`

