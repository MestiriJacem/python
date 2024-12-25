# liste_deroulante.py
import tkinter as tk
from tkinter import ttk  # Importation de ttk pour utiliser la combobox.

# Cours : Liste Déroulante (Combobox)
# Une combobox permet à l'utilisateur de sélectionner une option parmi une liste déroulante.
# Elle est créée à l'aide du widget Combobox de ttk, un sous-module de Tkinter.

# Fonction qui sera appelée lorsqu'une option est choisie
def option_selectionnee(event):
    selection = combobox.get()  # Récupère l'option sélectionnée.
    print(f"Option sélectionnée : {selection}")

# Création de la fenêtre principale
fenetre = tk.Tk()

# Définir le titre de la fenêtre
fenetre.title("Liste Déroulante Exemple")

# Créer une liste déroulante avec plusieurs options
options = ["Option 1", "Option 2", "Option 3"]
combobox = ttk.Combobox(fenetre, values=options, state="readonly")
combobox.pack(pady=20)

# Ajouter un événement lorsqu'une option est sélectionnée
combobox.bind("<<ComboboxSelected>>", option_selectionnee)

# Afficher la fenêtre
fenetre.mainloop()

# Cours : L'attribut state="readonly"
# En définissant l'état de la combobox à "readonly", l'utilisateur ne peut pas saisir de nouvelles valeurs.
# Il peut uniquement sélectionner une option parmi celles proposées.
