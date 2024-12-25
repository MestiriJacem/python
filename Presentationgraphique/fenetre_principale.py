# fenetre_principale.py
import tkinter as tk  # On importe la bibliothèque Tkinter pour la création d'interfaces graphiques.

# Cours : Fenêtre principale
# Une fenêtre principale est l'élément de base d'une application graphique en Python.
# Dans Tkinter, la fenêtre principale est représentée par un objet de la classe Tk().
# Elle permet d'afficher tous les widgets graphiques, tels que les labels, boutons, champs de texte, etc.

# Création de la fenêtre principale
fenetre = tk.Tk()  # Création de l'objet fenêtre.

# Définir le titre de la fenêtre
fenetre.title("Présentation Graphique - Python")  # On donne un titre à la fenêtre.

# Définir la taille de la fenêtre
fenetre.geometry("400x300")  # La fenêtre aura une taille de 400 pixels en largeur et 300 pixels en hauteur.

# Afficher la fenêtre
fenetre.mainloop()  # Cette ligne lance la boucle principale qui permet à la fenêtre de rester ouverte.

# Cours : La fonction mainloop()
# La fonction mainloop() permet à la fenêtre principale d'attendre des événements (clics, frappes clavier, etc.).
# Elle est essentielle pour maintenir l'application active et interactive.
