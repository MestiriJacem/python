# Fichier : portee_globale.py

compteur = 0  # Variable globale

def incrementer_compteur():
    """Incrémente une variable globale."""
    global compteur
    print(f"Valeur avant incrémentation : {compteur}")
    compteur += 1
    print(f"Valeur après incrémentation : {compteur}")

if __name__ == "__main__":
    print("\n--- Portée globale ---")
    incrementer_compteur()
    incrementer_compteur()
    print(f"Valeur finale du compteur : {compteur}")

# =======================================
# Points importants :
# - Une variable locale est définie et accessible uniquement dans la fonction où elle est créée.
# - Une variable globale peut être utilisée dans tout le programme.
# - Utilisez "global" pour modifier une variable globale à l'intérieur d'une fonction, mais
#   cette pratique est généralement déconseillée en faveur de solutions plus modulaires.
