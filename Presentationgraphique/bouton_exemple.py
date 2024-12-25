# bouton_exemple.py
import tkinter as tk

# Cours : Les Boutons
# Les boutons sont des éléments interactifs qui déclenchent des actions lorsqu'ils sont cliqués.
# Ils sont créés avec le widget Button() et peuvent être associés à une fonction à exécuter lors d'un clic.

# Fonction qui sera appelée lorsque le bouton sera cliqué
def afficher_message():
    print("Le bouton a été cliqué!")

# Création de la fenêtre principale
fenetre = tk.Tk()

# Définir le titre de la fenêtre
fenetre.title("Bouton Exemple")

# Créer un bouton avec un texte et une fonction à exécuter
button = tk.Button(fenetre, text="Cliquez ici", command=afficher_message)
button.pack(pady=20)  # Le bouton est placé dans la fenêtre.

# Afficher la fenêtre
fenetre.mainloop()

# Cours : L'attribut command
# L'attribut command permet d'associer une fonction qui sera exécutée lorsque le bouton est cliqué.
# Cette fonction est spécifiée en tant qu'argument lors de la création du bouton.
