# Fichier 1 : introduction_aux_objets.py
"""
Introduction aux objets en Python
Un objet est une instance d'une classe. Une classe est comme un plan (blueprint) pour créer des objets.
Les objets peuvent contenir des données (attributs) et des comportements (méthodes).
"""

# Définition d'une classe simple
class Person:
    """
    Une classe représentant une personne.
    """
    def __init__(self, name, age):
        """
        Constructeur qui initialise les attributs name et age.
        - name: Nom de la personne (str)
        - age: Âge de la personne (int)
        """
        self.name = name
        self.age = age

    def greet(self):
        """
        Méthode pour afficher un message de salutation.
        """
        print(f"Bonjour, je m'appelle {self.name} et j'ai {self.age} ans.")

# Création d'objets
person1 = Person("Alice", 30)  # Instance de la classe Person
person2 = Person("Bob", 25)  # Une autre instance de la classe Person

# Appel des méthodes
person1.greet()  # Affiche une salutation pour Alice
person2.greet()  # Affiche une salutation pour Bob

# Accès aux attributs
print(person1.name)  # Affiche le nom "Alice"
print(person2.age)   # Affiche l'âge 25
