lettres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffres = "0123456789"
speciaux = "!@#$%^&*()-_=+[]{};:,.<>?/|"
def melanger_chaine(chaine):
    liste = list(chaine)
    for i in range(len(liste)):
        # Échanger deux positions
        j = (i * 6 + 3) % len(liste)  # Simple formule pour générer un indice pseudo-aléatoire
        liste[i], liste[j] = liste[j], liste[i]
    return ''.join(liste)
def generer_mot_de_passe(longueur, inclure_speciaux):
    # Construire la liste de caractères autorisés
    caracteres = lettres + chiffres
    if inclure_speciaux:
        caracteres += speciaux

    # Mélanger pour obtenir des résultats variés
    caracteres = melanger_chaine(caracteres)

    # Construire le mot de passe
    mot_de_passe = ""
    for i in range(longueur):
        indice = (i * 4+ 2) % len(caracteres)  # Générer un pseudo-indice aléatoire
        mot_de_passe += caracteres[indice]
    return mot_de_passe
def main():
    print("=== Générateur de Mot de Passe ===")
    try:
        longueur = int(input("Entrez la longueur du mot de passe (minimum 6) : "))
        if longueur < 6:
            print("Erreur : La longueur doit être d'au moins 6 caractères.")
            return

        inclure_speciaux = input("Inclure des caractères spéciaux ? (oui/non) : ").lower() == "oui"

        mot_de_passe = generer_mot_de_passe(longueur, inclure_speciaux)
        print(f"Votre mot de passe généré : {mot_de_passe}")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide pour la longueur.")

main()
