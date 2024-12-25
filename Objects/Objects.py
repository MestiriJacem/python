# Python : Les Objets

# 1. Qu'est-ce qu'un Objet ?
# En Python, tout est un objet. Un objet est une instance d'une classe.
# Une classe est un modèle (ou une "blueprint") qui définit les propriétés et comportements des objets.

# Exemple simple de classe et objet :
class Personne:
    def __init__(self, nom, age):
        # Le constructeur initialise les propriétés de l'objet
        self.nom = nom
        self.age = age

    def se_presenter(self):
        # Une méthode pour afficher les informations de l'objet
        return f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans."

# Création d'objets (instances de la classe Personne)
personne1 = Personne("Alice", 30)
personne2 = Personne("Bob", 25)

# Utilisation des objets
print(personne1.se_presenter())  # Bonjour, je m'appelle Alice et j'ai 30 ans.
print(personne2.se_presenter())  # Bonjour, je m'appelle Bob et j'ai 25 ans.

# 2. Attributs et Méthodes
# Les objets ont :
# - des attributs : des variables qui stockent des données spécifiques à l'objet.
# - des méthodes : des fonctions définies dans la classe qui peuvent être appelées sur les objets.

# Exemple : Modification des attributs
personne1.age = 31  # Modification de l'attribut 'age'
print(personne1.se_presenter())  # Bonjour, je m'appelle Alice et j'ai 31 ans.

# 3. Les Propriétés (Getters et Setters)
# Utiliser des getters et setters pour contrôler l'accès aux attributs.
class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    @property
    def aire(self):
        return self.largeur * self.hauteur

    @aire.setter
    def aire(self, valeur):
        raise AttributeError("L'aire est une propriété calculée, vous ne pouvez pas la définir directement.")

# Création d'un rectangle
rectangle = Rectangle(5, 10)
print(rectangle.aire)  # 50

# 4. Héritage
# Une classe peut hériter d'une autre classe pour réutiliser et étendre ses fonctionnalités.
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        raise NotImplementedError("Cette méthode doit être implémentée par une sous-classe.")

class Chien(Animal):
    def parler(self):
        return "Woof!"

class Chat(Animal):
    def parler(self):
        return "Meow!"

# Création d'objets animaux
chien = Chien("Rex")
chat = Chat("Mimi")

print(chien.parler())  # Woof!
print(chat.parler())   # Meow!

# 5. Polymorphisme
# Le polymorphisme permet d'utiliser une interface commune pour différents types d'objets.
animaux = [chien, chat]
for animal in animaux:
    print(f"{animal.nom} dit : {animal.parler()}")

# 6. Méthodes Spéciales (Dunder Methods)
# Les "dunder methods" permettent de personnaliser le comportement d'un objet pour des opérations spécifiques.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, autre):
        return Point(self.x + autre.x, self.y + autre.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Utilise __add__
print(p3)    # Point(4, 6)

# Résumé :
# - Une classe est un modèle pour créer des objets.
# - Les objets ont des attributs et des méthodes.
# - L'héritage et le polymorphisme permettent de réutiliser et d'étendre le code.
# - Les méthodes spéciales permettent de personnaliser le comportement des objets.