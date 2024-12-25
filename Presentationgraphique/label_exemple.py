# label_exemple.py
import tkinter as tk

# Cours : Les Labels
# Les labels sont des éléments graphiques qui affichent du texte ou des images statiques dans une fenêtre.
# Ils sont souvent utilisés pour donner des instructions ou afficher des informations dans l'interface.

# Création de la fenêtre principale
fenetre = tk.Tk()

# Définir le titre de la fenêtre
fenetre.title("Label Exemple")

# Créer un label avec un texte
label = tk.Label(fenetre, text="Bonjour, bienvenue dans le cours Python !", font=("Helvetica", 14))
label.pack(pady=20)  # Le label est placé dans la fenêtre avec un espace vertical (pady).

# Afficher la fenêtre
fenetre.mainloop()

# Cours : Le widget Label
# Le widget Label est créé avec la méthode Label() et accepte plusieurs paramètres comme :
# - text : le texte à afficher.
# - font : la police et la taille du texte.
# - padx/pady : marges horizontales et verticales autour du texte.
