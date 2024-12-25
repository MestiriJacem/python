# --- Projet 9 : Mini Système de Banque ---
# Énoncé : Créez un programme qui simule un système bancaire.
# L'utilisateur peut déposer de l'argent, retirer de l'argent, et consulter son solde.

# Initialisation du solde
solde = 0

# Fonction pour effectuer un dépôt
def deposer():
    global solde  # Permet de modifier la variable globale
    montant = float(input("Entrez le montant à déposer : "))
    solde += montant
    print(f"{montant}€ déposés. Nouveau solde : {solde}€.")

# Fonction pour effectuer un retrait
def retirer():
    global solde
    montant = float(input("Entrez le montant à retirer : "))
    if montant <= solde:  # Vérifie si le solde est suffisant
        solde -= montant
        print(f"{montant}€ retirés. Nouveau solde : {solde}€.")
    else:
        print("Fonds insuffisants.")

# Fonction pour consulter le solde
def consulter_solde():
    print(f"Solde actuel : {solde}€.")

# Menu principal
while True:
    print("\n1. Déposer\n2. Retirer\n3. Consulter le solde\n4. Quitter")
    choix = input("Votre choix : ")
    if choix == "1":
        deposer()
    elif choix == "2":
        retirer()
    elif choix == "3":
        consulter_solde()
    elif choix == "4":
        print("Merci d'avoir utilisé notre banque. À bientôt !")
        break
    else:
        print("Choix invalide.")
