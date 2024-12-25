# champ_texte_exemple.py
import tkinter as tk

# Cours : Les Champs de Texte (Entry)
# Les champs de texte sont des widgets qui permettent à l'utilisateur de saisir du texte.
# Dans Tkinter, ces widgets sont représentés par la classe Entry().
# On peut récupérer ou modifier le texte de ces champs avec des méthodes comme get() et insert().

# Fonction pour récupérer le texte du champ et l'afficher
def afficher_texte():
    texte = champ_texte.get()  # Récupère le texte du champ.
    print(f"Le texte entré est : {texte}")

# Création de la fenêtre principale
fenetre = tk.Tk()

# Définir le titre de la fenêtre
fenetre.title("Champ de texte Exemple")

# Créer un champ de texte
champ_texte = tk.Entry(fenetre, font=("Helvetica", 14))
champ_texte.pack(pady=20)  # Le champ est placé dans la fenêtre.

# Créer un bouton pour afficher le texte
button = tk.Button(fenetre, text="Afficher le texte", command=afficher_texte)
button.pack()

# Afficher la fenêtre
fenetre.mainloop()

# Cours : Les méthodes get() et insert()
# - get() permet de récupérer le texte du champ de texte.
# - insert() permet d'ajouter du texte à une position spécifiée dans le champ de texte.
