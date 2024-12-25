# Fichier 5 : abstraction.py
"""
Abstraction en Python
L'abstraction cache les détails complexes et montre uniquement l'essentiel.
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """
        Calcule et retourne l'aire de la forme.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calcule et retourne le périmètre de la forme.
        """
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur.
        - width: Largeur du rectangle (float)
        - height: Hauteur du rectangle (float)
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Retourne l'aire du rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Retourne le périmètre du rectangle.
        """
        return 2 * (self.width + self.height)

# Utilisation
rect = Rectangle(5, 10)  # Rectangle de largeur 5 et hauteur 10
print("Aire:", rect.area())  # Affiche : Aire: 50
print("Périmètre:", rect.perimeter())  # Affiche : Périmètre: 30