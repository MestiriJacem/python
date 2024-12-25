# --- Projet 5 : Système de Gestion des Étudiants ---
# Énoncé : Créez un programme pour gérer une liste d'étudiants.
# Chaque étudiant a un nom et une note, et le programme permet d'ajouter des étudiants,
# afficher la liste et calculer la moyenne de la classe.

etudiants = []  # Liste pour stocker les étudiants

# Fonction pour ajouter un étudiant
def ajouter_etudiant():
    nom = input("Entrez le nom de l'étudiant : ")
    note = float(input("Entrez la note de l'étudiant : "))
    etudiants.append({"nom": nom, "note": note})

# Fonction pour afficher les étudiants
def afficher_etudiants():
    if not etudiants:  # Vérification si la liste est vide
        print("Aucun étudiant.")
    else:
        for etudiant in etudiants:
            print(f"{etudiant['nom']} - {etudiant['note']}")

# Fonction pour calculer la moyenne
def calculer_moyenne():
    if not etudiants:
        print("Aucune note disponible.")
    else:
        moyenne = sum(etudiant['note'] for etudiant in etudiants) / len(etudiants)
        print(f"Moyenne de la classe : {moyenne:.2f}")

# Menu principal
while True:
    print("\n1. Ajouter un étudiant\n2. Afficher les étudiants\n3. Calculer la moyenne\n4. Quitter")
    choix = input("Votre choix : ")
    if choix == "1":
        ajouter_etudiant()
    elif choix == "2":
        afficher_etudiants()
    elif choix == "3":
        calculer_moyenne()
    elif choix == "4":
        break
    else:
        print("Choix invalide.")
