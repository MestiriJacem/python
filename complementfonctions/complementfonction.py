# --- INTRODUCTION AUX FONCTIONS EN PYTHON ---

# Une fonction est un bloc de code réutilisable qui exécute une tâche spécifique.
# Elle peut prendre des entrées (arguments) et renvoyer une sortie (valeur de retour).

# --- Définir une fonction simple ---
def saluer():
    """
    Une fonction simple qui affiche un message de bienvenue.
    """
    print("Bonjour, bienvenue dans ce cours sur les fonctions en Python !")

# Appel de la fonction
saluer()


# --- Fonction avec des paramètres ---
def saluer_personnalise(nom):
    """
    Affiche un message de bienvenue personnalisé.
    :param nom: str, le nom de la personne à saluer
    """
    print(f"Bonjour {nom}, ravi de vous rencontrer !")

# Appel de la fonction avec un argument
saluer_personnalise("Alice")


# --- Fonction avec une valeur de retour ---
def carre(nombre):
    """
    Calcule le carré d'un nombre.
    :param nombre: int ou float
    :return: int ou float, le carré du nombre
    """
    return nombre ** 2

# Appel de la fonction et stockage du résultat
resultat = carre(4)
print(f"Le carré de 4 est {resultat}")


# --- Fonction avec des paramètres par défaut ---
def saluer_formel(nom="invité"):
    """
    Affiche un message de bienvenue formel avec un paramètre par défaut.
    :param nom: str, le nom de la personne (par défaut "invité")
    """
    print(f"Bonjour {nom}, bienvenue dans cet événement formel.")

# Appels de la fonction
saluer_formel()          # Utilise la valeur par défaut
saluer_formel("Claire")  # Fournit un argument


# --- Fonction avec des arguments multiples ---
def additionner(a, b):
    """
    Additionne deux nombres.
    :param a: int ou float
    :param b: int ou float
    :return: int ou float, la somme des deux nombres
    """
    return a + b

# Appel de la fonction
somme = additionner(5, 7)
print(f"La somme de 5 et 7 est {somme}")


# --- Fonctions Lambda (fonctions anonymes) ---
# Une fonction lambda est une fonction simple, définie en une seule ligne, sans nom.

# Exemple : fonction lambda pour calculer le carré d'un nombre
carre_lambda = lambda x: x ** 2
print(f"Le carré de 5 (lambda) est {carre_lambda(5)}")

# Exemple : addition de deux nombres
addition_lambda = lambda x, y: x + y
print(f"La somme de 3 et 8 (lambda) est {addition_lambda(3, 8)}")


# --- Fonctions avec un nombre variable d'arguments ---
def additionner_tous(*nombres):
    """
    Additionne un nombre variable d'arguments.
    :param nombres: tuple, une liste de nombres
    :return: int ou float, la somme de tous les nombres
    """
    return sum(nombres)

# Appels de la fonction
print(f"Somme de 1, 2, 3 : {additionner_tous(1, 2, 3)}")
print(f"Somme de 4, 5, 6, 7 : {additionner_tous(4, 5, 6, 7)}")


# --- Fonction avec des mots-clés d'arguments ---
def afficher_informations(**infos):
    """
    Affiche des informations sous forme de mots-clés.
    :param infos: dict, informations sous forme de clé-valeur
    """
    for cle, valeur in infos.items():
        print(f"{cle}: {valeur}")

# Appel de la fonction
afficher_informations(nom="Jean", age=30, ville="Paris")
