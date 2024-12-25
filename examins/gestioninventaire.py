# --- Projet 6 : Gestion d'un Inventaire ---
# Énoncé : Créez un programme qui gère un inventaire de produits.
# L'utilisateur peut ajouter des produits, afficher l'inventaire, et supprimer des produits.

# Initialisation de l'inventaire sous forme de dictionnaire
inventaire = {}

# Fonction pour ajouter un produit à l'inventaire
def ajouter_produit():
    produit = input("Nom du produit : ")
    quantite = int(input("Quantité : "))
    # Mise à jour de l'inventaire (ajoute ou met à jour la quantité)
    inventaire[produit] = inventaire.get(produit, 0) + quantite

# Fonction pour afficher l'inventaire
def afficher_inventaire():
    print("\nInventaire :")
    if not inventaire:  # Vérifie si l'inventaire est vide
        print("L'inventaire est vide.")
    else:
        for produit, quantite in inventaire.items():
            print(f"{produit}: {quantite}")

# Fonction pour supprimer un produit
def supprimer_produit():
    produit = input("Produit à supprimer : ")
    if produit in inventaire:  # Vérifie si le produit existe
        del inventaire[produit]
        print(f"{produit} a été supprimé.")
    else:
        print("Produit introuvable.")

# Menu principal
while True:
    print("\n1. Ajouter un produit\n2. Afficher l'inventaire\n3. Supprimer un produit\n4. Quitter")
    choix = input("Votre choix : ")
    if choix == "1":
        ajouter_produit()
    elif choix == "2":
        afficher_inventaire()
    elif choix == "3":
        supprimer_produit()
    elif choix == "4":
        break
    else:
        print("Choix invalide.")
