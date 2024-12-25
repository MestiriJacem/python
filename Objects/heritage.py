"""
Héritage en Python
L'héritage permet de créer une nouvelle classe à partir d'une classe existante.
La nouvelle classe (classe enfant) hérite des attributs et méthodes de la classe parente.
"""

# Classe parente
class Animal:
    def __init__(self, name):
        """
        Initialisation de l'attribut name.
        - name: Nom de l'animal (str)
        """
        self.name = name

    def speak(self):
        """
        Méthode par défaut pour la classe Animal.
        """
        return "Je ne sais pas quoi dire!"

# Classe enfant
class Dog(Animal):
    def speak(self):
        """
        Méthode spécialisée pour la classe Dog.
        """
        return "hab! hab!"

class Cat(Animal):
    def speak(self):
        """
        Méthode spécialisée pour la classe Cat.
        """
        return "Meow!"

# Création des objets
dog = Dog("Rex")  # Un chien nommé Rex
cat = Cat("Whiskers")  # Un chat nommé Whiskers

print(dog.name, "dit", dog.speak())  # Affiche : Rex dit Woof! Woof!
print(cat.name, "dit", cat.speak())  # Affiche : Whiskers dit Meow!
