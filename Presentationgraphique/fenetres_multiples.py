# fenetre_multiple.py
import tkinter as tk

# Cours : Fenêtres Secondaires (Toplevel)
# Les fenêtres secondaires sont des fenêtres supplémentaires ouvertes à partir de la fenêtre principale.
# Elles sont créées avec la classe Toplevel() et peuvent être utilisées pour afficher des informations ou interagir avec l'utilisateur.

# Fonction pour ouvrir une nouvelle fenêtre
def ouvrir_fenetre_secondaire():
    fenetre_secondaire = tk.Toplevel()  # Crée une nouvelle fenêtre secondaire.
    fenetre_secondaire.title("Fenêtre Secondaire")
    label_secondaire = tk.Label(fenetre_secondaire, text="Ceci est une fenêtre secondaire", font=("Helvetica", 14))
    label_secondaire.pack(pady=20)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Fenêtre Principale")

# Créer un bouton pour ouvrir une nouvelle fenêtre
button_ouvrir = tk.Button(fenetre, text="Ouvrir une fenêtre secondaire", command=ouvrir_fenetre_secondaire)
button_ouvrir.pack(pady=20)

# Afficher la fenêtre
fenetre.mainloop()

# Cours : La classe Toplevel()
# La classe Toplevel() permet de créer une fenêtre secondaire indépendante de la fenêtre principale.
# Elle peut être utilisée pour créer des dialogues, des pop-ups ou des fenêtres supplémentaires dans l'application.
