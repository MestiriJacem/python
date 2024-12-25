# Fichier 3 : encapsulation.py
"""
Encapsulation en Python
L'encapsulation consiste à restreindre l'accès direct aux attributs d'un objet pour les protéger.
"""

class BankAccount:
    def __init__(self, owner, balance):
        """
        Initialise un compte bancaire.
        - owner: Propriétaire du compte (str)
        - balance: Solde initial (float)
        """
        self.owner = owner
        self.__balance = balance  # Attribut privé

    def deposit(self, amount):
        """
        Ajoute un montant au solde.
        - amount: Montant à déposer (float)
        """
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        """
        Retire un montant du solde si suffisant.
        - amount: Montant à retirer (float)
        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        """
        Retourne le solde actuel du compte.
        """
        return self.__balance

# Création d'un compte bancaire
account = BankAccount("Alice", 1000)  # Compte avec un solde initial de 1000
account.deposit(500)  # Dépose 500
account.withdraw(300)  # Retire 300

print("Solde:", account.get_balance())  # Affiche : Solde: 1200
#print(account.__balance)  # Provoquera une erreur car __balance est privé
