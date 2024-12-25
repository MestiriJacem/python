# --- Projet 7 : Vérificateur de Palindrome ---
# Énoncé : Créez un programme qui vérifie si un mot ou une phrase est un palindrome.
# Un palindrome est une chaîne qui se lit de la même façon à l'endroit et à l'envers.

# Fonction pour vérifier si un texte est un palindrome
def est_palindrome(texte):
    # On retire les espaces et on met tout en minuscules pour uniformiser
    texte = texte.replace(" ", "").lower()
    # Comparaison du texte avec son inverse
    return texte == texte[::-1]

# Entrée utilisateur
texte = input("Entrez un mot ou une phrase : ")

# Vérification et affichage du résultat
if est_palindrome(texte):
    print("C'est un palindrome.")
else:
    print("Ce n'est pas un palindrome.")
