# Projet de Programmation Graphique en Python
# Objectif : Créer une petite application graphique permettant de gérer une liste de tâches.
# L'utilisateur pourra :
# 1. Ajouter une tâche.
# 2. Supprimer une tâche sélectionnée.
# 3. Afficher toutes les tâches dans une liste graphique.
# 4. Quitter l'application.

import tkinter as tk
from tkinter import messagebox

# Fonctionnalités de l'application
def ajouter_tache():
    """Ajoute une tâche à la liste."""
    tache = entree.get()
    if tache:
        liste_taches.insert(tk.END, tache)
        entree.delete(0, tk.END)
    else:
        messagebox.showwarning("Attention", "Veuillez entrer une tâche.")

def supprimer_tache():
    """Supprime la tâche sélectionnée dans la liste."""
    try:
        index_selection = liste_taches.curselection()[0]
        liste_taches.delete(index_selection)
    except IndexError:
        messagebox.showerror("Erreur", "Aucune tâche sélectionnée.")

def quitter_application():
    """Ferme l'application après confirmation de l'utilisateur."""
    if messagebox.askyesno("Quitter", "Voulez-vous vraiment quitter ?"):
        fenetre.destroy()

# Configuration de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Gestionnaire de Tâches")
fenetre.geometry("400x400")

# Widgets de l'application
label = tk.Label(fenetre, text="Entrez une nouvelle tâche :", font=("Arial", 12))
label.pack(pady=10)

entree = tk.Entry(fenetre, width=30, font=("Arial", 12))
entree.pack(pady=10)

bouton_ajouter = tk.Button(fenetre, text="Ajouter", command=ajouter_tache, font=("Arial", 12))
bouton_ajouter.pack(pady=5)

liste_taches = tk.Listbox(fenetre, width=40, height=10, font=("Arial", 12))
liste_taches.pack(pady=10)

bouton_supprimer = tk.Button(fenetre, text="Supprimer", command=supprimer_tache, font=("Arial", 12), bg="red", fg="white")
bouton_supprimer.pack(pady=5)

bouton_quitter = tk.Button(fenetre, text="Quitter", command=quitter_application, font=("Arial", 12), bg="gray", fg="white")
bouton_quitter.pack(pady=20)

# Lancer la boucle principale
fenetre.mainloop()

# Résumé :
# Ce projet utilise Tkinter pour créer une interface graphique simple.
# Il comprend des champs d'entrée, des boutons et une liste pour interagir avec les tâches.
# Les fonctions permettent d'ajouter, supprimer et gérer les tâches efficacement.
