# --- PROGRAMMATION ORIENTÉE OBJET (POO) EN PYTHON ---

# La POO est un paradigme de programmation qui permet de modéliser des concepts du monde réel
# sous forme d'objets. Un objet est une instance d'une classe, qui définit ses propriétés (attributs)
# et son comportement (méthodes).

# --- Définir une classe simple ---
class Personne:
    """
    Une classe représentant une personne.
    """

    def __init__(self, nom, age):
        """
        Constructeur de la classe Personne.
        :param nom: str, le nom de la personne
        :param age: int, l'âge de la personne
        """
        self.nom = nom  # Attribut instance : nom
        self.age = age  # Attribut instance : âge

    def se_presenter(self):
        """
        Méthode pour afficher les informations de la personne.
        """
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans.")


# Création d'une instance (objet) de la classe
personne1 = Personne("Alice", 30)
personne1.se_presenter()  # Appelle la méthode de l'objet


# --- Héritage ---
class Etudiant(Personne):
    """
    Une classe représentant un étudiant, qui hérite de Personne.
    """

    def __init__(self, nom, age, universite):
        """
        Constructeur de la classe Etudiant.
        :param universite: str, le nom de l'université
        """
        super().__init__(nom, age)  # Appelle le constructeur de la classe parent
        self.universite = universite  # Nouvel attribut pour Etudiant

    def se_presenter(self):
        """
        Méthode redéfinie pour inclure l'université.
        """
        super().se_presenter()
        print(f"Je suis étudiant à l'université {self.universite}.")


# Création d'une instance d'Étudiant
etudiant1 = Etudiant("Bob", 20, "Sorbonne")
etudiant1.se_presenter()


# --- Encapsulation ---
class CompteBancaire:
    """
    Une classe représentant un compte bancaire.
    """

    def __init__(self, titulaire, solde):
        self.titulaire = titulaire  # Attribut public
        self.__solde = solde  # Attribut privé

    def deposer(self, montant):
        """
        Dépose un montant sur le compte.
        """
        if montant > 0:
            self.__solde += montant
            print(f"{montant}€ déposés. Nouveau solde : {self.__solde}€.")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        """
        Retire un montant du compte si possible.
        """
        if montant > 0 and montant <= self.__solde:
            self.__solde -= montant
            print(f"{montant}€ retirés. Nouveau solde : {self.__solde}€.")
        else:
            print("Retrait impossible.")

    def afficher_solde(self):
        """
        Affiche le solde actuel (accès contrôlé).
        """
        print(f"Le solde de {self.titulaire} est : {self.__solde}€.")


# Création d'une instance de CompteBancaire
compte = CompteBancaire("Charlie", 500)
compte.afficher_solde()
compte.deposer(200)
compte.retirer(100)


# Tentative d'accès à un attribut privé (provoque une erreur)
# print(compte.__solde)


# --- Polymorphisme ---
class Animal:
    """
    Une classe représentant un animal.
    """

    def parler(self):
        """
        Méthode à surcharger dans les classes enfants.
        """
        pass


class Chien(Animal):
    def parler(self):
        print("Woof!")


class Chat(Animal):
    def parler(self):
        print("Meow!")


# Utilisation du polymorphisme
animaux = [Chien(), Chat()]
for animal in animaux:
    animal.parler()


# --- Méthodes et attributs de classe ---
class Math:
    """
    Une classe utilitaire pour des opérations mathématiques.
    """

    PI = 3.14159  # Attribut de classe

    @classmethod
    def carre(cls, x):
        """
        Retourne le carré d'un nombre.
        """
        return x ** 2

    @staticmethod
    def addition(a, b):
        """
        Additionne deux nombres.
        """
        return a + b


# Accès aux attributs et méthodes de classe
print(f"Pi : {Math.PI}")
print(f"Carré de 5 : {Math.carre(5)}")
print(f"Addition de 3 et 4 : {Math.addition(3, 4)}")
