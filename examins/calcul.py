# --- Projet 1 : Calculatrice de Base ---
# Énoncé : Créez un programme qui fonctionne comme une calculatrice simple.
# L'utilisateur choisit une opération (addition, soustraction, multiplication, division) et entre deux nombres.
# Le programme retourne le résultat de l'opération.

# Définition des fonctions pour chaque opération
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:  # Vérification pour éviter une division par zéro
        return a / b
    else:
        return "Erreur : Division par zéro impossible."

# Menu pour choisir l'opération
print("Calculatrice : ")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")

# Entrée de l'utilisateur
choix = input("Choisissez une opération (1/2/3/4) : ")
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le second nombre : "))

# Appel de la fonction appropriée en fonction du choix
if choix == "1":
    print("Résultat :", addition(a, b))
elif choix == "2":
    print("Résultat :", soustraction(a, b))
elif choix == "3":
    print("Résultat :", multiplication(a, b))
elif choix == "4":
    print("Résultat :", division(a, b))
else:
    print("Choix invalide.")
