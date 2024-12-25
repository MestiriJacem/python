# Cours : Structure d'un programme Python
# ========================================
# En Python, un programme est généralement organisé de manière à être clair et lisible.
# Voici les principales sections d'un programme Python :

# 1. Importation des modules nécessaires
# 2. Définition des fonctions
# 3. Code principal (point d'entrée du programme)

# Exemple pratique dans un fichier séparé : structure_programme.py

# =======================================
# Fichier : structure_programme.py
import math

def calculer_hypotenuse(a, b):
    """Calcule l'hypoténuse d'un triangle rectangle."""
    return math.sqrt(a**2 + b**2)

if __name__ == "__main__":
    cote_a = float(input("Entrez la longueur du côté a : "))
    cote_b = float(input("Entrez la longueur du côté b : "))
    resultat = calculer_hypotenuse(cote_a, cote_b)
    print(f"L'hypoténuse est : {resultat}")

# =======================================
# À noter :
# - La structure "if __name__ == '__main__':" est utilisée pour indiquer le point d'entrée
#   lorsque le fichier est exécuté directement, plutôt qu'importé comme module.

# =======================================