# Fichier 4 : polymorphisme.py
"""
Polymorphisme en Python
Le polymorphisme permet d'utiliser une interface commune pour des objets de classes différentes.
"""

class Bird:
    def fly(self):
        """
        Méthode par défaut pour les oiseaux.
        """
        return "Je peux voler."

class Penguin(Bird):
    def fly(self):
        """
        Méthode spécialisée pour les pingouins.
        """
        return "Je ne peux pas voler, mais je peux nager."

def bird_fly(bird):
    """
    Fonction qui affiche le comportement de vol d'un oiseau.
    - bird: Instance d'une classe dérivée de Bird
    """
    print(bird.fly())

# Utilisation du polymorphisme
sparrow = Bird()  # Un moineau
penguin = Penguin()  # Un pingouin

bird_fly(sparrow)  # Affiche : Je peux voler.
bird_fly(penguin)  # Affiche : Je ne peux pas voler, mais je peux nager.