# Python : La Gestion des Exceptions

# 1. Qu'est-ce qu'une Exception ?
# Une exception est une erreur qui se produit pendant l'exécution d'un programme.
# En Python, lorsqu'une exception se produit, le programme s'arrête sauf si elle est gérée explicitement.

# Exemple simple d'exception non gérée :
# print(10 / 0)  # Provoque une exception : ZeroDivisionError

# 2. Gestion des Exceptions avec try/except
# Utilisez try et except pour intercepter les exceptions et éviter que le programme ne plante.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Erreur : Division par zéro !")

# 3. Gestion de Multiples Exceptions
# Vous pouvez gérer différents types d'exceptions avec plusieurs blocs except.
try:
    x = int("abc")
except ValueError:
    print("Erreur : Conversion invalide en entier.")
except ZeroDivisionError:
    print("Erreur : Division par zéro !")

# 4. Le Bloc else
# Le bloc else s'exécute si aucune exception ne se produit dans le bloc try.
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Erreur : Division par zéro !")
else:
    print(f"Résultat : {result}")

# 5. Le Bloc finally
# Le bloc finally s'exécute toujours, qu'une exception se produise ou non.
try:
    file = open("fichier_inexistant.txt", "r")
except FileNotFoundError:
    print("Erreur : Fichier introuvable.")
finally:
    print("Bloc finally exécuté.")

# 6. Lever une Exception
# Vous pouvez lever une exception manuellement avec l'instruction raise.
try:
    age = -1
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif.")
except ValueError as e:
    print(f"Erreur : {e}")

# 7. Définir Vos Propres Exceptions
# Vous pouvez définir des exceptions personnalisées en créant des classes qui héritent de Exception.
class MonException(Exception):
    pass

try:
    raise MonException("Ceci est une exception personnalisée.")
except MonException as e:
    print(f"MonException attrapée : {e}")

# 8. Les Bonnes Pratiques
# - Gérer uniquement les exceptions que vous attendez.
# - Ne pas utiliser un bloc except trop général.
try:
    print(10 / "string")
except Exception as e:  # Trop général, à éviter dans la pratique.
    print(f"Erreur : {e}")

# Résumé :
# - Les exceptions permettent de gérer les erreurs sans arrêter brutalement le programme.
# - Utilisez try/except/else/finally pour structurer la gestion des erreurs.
# - Vous pouvez lever vos propres exceptions ou définir des exceptions personnalisées.
