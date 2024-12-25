# --- Projet 10 : Gestion d'une Bibliothèque ---
# Énoncé : Créez un programme pour gérer une bibliothèque.
# L'utilisateur peut ajouter des livres, afficher la liste des livres, rechercher un livre, et le supprimer.

# Initialisation de la bibliothèque
bibliotheque = []

# Fonction pour ajouter un livre
def ajouter_livre():
    titre = input("Entrez le titre du livre : ")
    auteur = input("Entrez l'auteur du livre : ")
    bibliotheque.append({"titre": titre, "auteur": auteur})
    print(f'Le livre "{titre}" a été ajouté.')

# Fonction pour afficher tous les livres
def afficher_livres():
    if not bibliotheque:  # Vérifie si la bibliothèque est vide
        print("Aucun livre dans la bibliothèque.")
    else:
        print("Liste des livres :")
        for i, livre in enumerate(bibliotheque, start=1):
            print(f'{i}. {livre["titre"]} - {livre["auteur"]}')

# Fonction pour rechercher un livre par son titre
def rechercher_livre():
    titre = input("Entrez le titre du livre à rechercher : ")
    for livre in bibliotheque:
        if livre["titre"].lower() == titre.lower():  # Recherche insensible à la casse
            print(f'Le livre "{livre["titre"]}" de {livre["auteur"]} est disponible.')
            return
    print(f'Le livre "{titre}" n\'a pas été trouvé.')

# Fonction pour supprimer un livre par son titre
def supprimer_livre():
    titre = input("Entrez le titre du livre à supprimer : ")
    for livre in bibliotheque:
        if livre["titre"].lower() == titre.lower():
            bibliotheque.remove(livre)
            print(f'Le livre "{titre}" a été supprimé.')
            return
    print(f'Le livre "{titre}" n\'a pas été trouvé.')

# Menu principal
while True:
    print("\n1. Ajouter un livre\n2. Afficher les livres\n3. Rechercher un livre\n4. Supprimer un livre\n5. Quitter")
    choix = input("Votre choix : ")
    if choix == "1":
        ajouter_livre()
    elif choix == "2":
        afficher_livres()
    elif choix == "3":
        rechercher_livre()
    elif choix == "4":
        supprimer_livre()
    elif choix == "5":
        print("Merci d'avoir utilisé la gestion de bibliothèque. À bientôt !")
        break
    else:
        print("Choix invalide.")
