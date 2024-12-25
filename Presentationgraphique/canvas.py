# canvas_exemple.py
import tkinter as tk

# Cours : Le Canevas (Canvas)
# Le canevas est un widget très puissant qui permet de dessiner des formes géométriques, des images, et de créer des animations.
# Il permet aussi d'afficher des éléments interactifs comme des graphiques ou des diagrammes.

# Création de la fenêtre principale
fenetre = tk.Tk()

# Définir le titre de la fenêtre
fenetre.title("Canevas Exemple")

# Création d'un canevas dans la fenêtre
canvas = tk.Canvas(fenetre, width=400, height=300, bg="lightblue")
canvas.pack()

# Dessiner un rectangle sur le canevas
canvas.create_rectangle(50, 50, 350, 250, outline="black", fill="yellow")

# Afficher la fenêtre
fenetre.mainloop()

# Cours : Méthodes du Canevas
# - create_rectangle(x1, y1, x2, y2) : crée un rectangle avec les coordonnées de deux coins opposés.
# - create_line(x1, y1, x2, y2) : crée une ligne entre deux points.
# Le canevas peut également afficher du texte, des images et d'autres formes.
