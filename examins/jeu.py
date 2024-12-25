# --- Projet 4 : Jeu du Nombre Mystère ---
# Énoncé : Créez un jeu où l'utilisateur doit deviner un nombre entre 1 et 100.
# L'ordinateur génère un nombre aléatoire, et l'utilisateur reçoit des indices "trop grand" ou "trop petit".

import random

def jeu_nombre_mystere():
    # Génération d'un nombre aléatoire
    nombre = random.randint(1, 100)
    tentatives = 0  # Compteur de tentatives

    print("Devinez le nombre entre 1 et 100.")
    while True:
        # Demande d'une tentative
        tentative = int(input("Votre tentative : "))
        tentatives += 1
        # Vérification de la tentative
        if tentative < nombre:
            print("Trop petit !")
        elif tentative > nombre:
            print("Trop grand !")
        else:
            print(f"Bravo ! Vous avez trouvé en {tentatives} tentatives.")
            break

# Lancement du jeu
jeu_nombre_mystere()
