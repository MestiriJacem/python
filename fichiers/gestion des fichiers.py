# Projet : Gestion des Fichiers en Python
# Objectif : Développer un programme pour gérer des fichiers dans un dossier donné.
# L'utilisateur pourra :
# 1. Créer un nouveau fichier.
# 2. Lire le contenu d'un fichier existant.
# 3. Ajouter du contenu à un fichier existant.
# 4. Supprimer un fichier.

import os
from tkinter import Tk, Label, Entry, Button, Listbox, END, messagebox

# Fonctionnalités liées aux fichiers
def creer_fichier():
    """Crée un nouveau fichier dans le dossier courant."""
    nom_fichier = entree_nom.get()
    if nom_fichier:
        try:
            with open(nom_fichier, 'x') as f:
                pass
            messagebox.showinfo("Succès", f"Le fichier '{nom_fichier}' a été créé.")
            actualiser_liste_fichiers()
        except FileExistsError:
            messagebox.showerror("Erreur", "Le fichier existe déjà.")
    else:
        messagebox.showwarning("Attention", "Veuillez entrer un nom de fichier.")

def lire_fichier():
    """Lit et affiche le contenu du fichier sélectionné."""
    try:
        fichier_selectionne = liste_fichiers.get(liste_fichiers.curselection()[0])
        with open(fichier_selectionne, 'r') as f:
            contenu = f.read()
        messagebox.showinfo(f"Contenu de {fichier_selectionne}", contenu)
    except IndexError:
        messagebox.showerror("Erreur", "Aucun fichier sélectionné.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de lire le fichier : {e}")

def ajouter_contenu():
    """Ajoute du contenu à un fichier existant."""
    try:
        fichier_selectionne = liste_fichiers.get(liste_fichiers.curselection()[0])
        contenu = entree_contenu.get()
        if contenu:
            with open(fichier_selectionne, 'a') as f:
                f.write(contenu + '\n')
            messagebox.showinfo("Succès", f"Contenu ajouté au fichier '{fichier_selectionne}'.")
        else:
            messagebox.showwarning("Attention", "Veuillez entrer du contenu à ajouter.")
    except IndexError:
        messagebox.showerror("Erreur", "Aucun fichier sélectionné.")

def supprimer_fichier():
    """Supprime le fichier sélectionné."""
    try:
        fichier_selectionne = liste_fichiers.get(liste_fichiers.curselection()[0])
        if messagebox.askyesno("Confirmation", f"Voulez-vous vraiment supprimer '{fichier_selectionne}' ?"):
            os.remove(fichier_selectionne)
            messagebox.showinfo("Succès", f"Le fichier '{fichier_selectionne}' a été supprimé.")
            actualiser_liste_fichiers()
    except IndexError:
        messagebox.showerror("Erreur", "Aucun fichier sélectionné.")

def actualiser_liste_fichiers():
    """Met à jour la liste des fichiers dans le dossier courant."""
    liste_fichiers.delete(0, END)
    fichiers = [f for f in os.listdir('.') if os.path.isfile(f)]
    for fichier in fichiers:
        liste_fichiers.insert(END, fichier)

# Interface graphique
fenetre = Tk()
fenetre.title("Gestion des Fichiers")
fenetre.geometry("500x500")

# Widgets de l'application
label_nom = Label(fenetre, text="Nom du fichier :", font=("Arial", 12))
label_nom.pack(pady=5)

entree_nom = Entry(fenetre, width=40, font=("Arial", 12))
entree_nom.pack(pady=5)

bouton_creer = Button(fenetre, text="Créer un fichier", command=creer_fichier, font=("Arial", 12))
bouton_creer.pack(pady=5)

label_contenu = Label(fenetre, text="Contenu à ajouter :", font=("Arial", 12))
label_contenu.pack(pady=5)

entree_contenu = Entry(fenetre, width=40, font=("Arial", 12))
entree_contenu.pack(pady=5)

bouton_ajouter = Button(fenetre, text="Ajouter du contenu", command=ajouter_contenu, font=("Arial", 12))
bouton_ajouter.pack(pady=5)

liste_fichiers = Listbox(fenetre, width=50, height=15, font=("Arial", 12))
liste_fichiers.pack(pady=10)

bouton_lire = Button(fenetre, text="Lire le fichier", command=lire_fichier, font=("Arial", 12))
bouton_lire.pack(pady=5)

bouton_supprimer = Button(fenetre, text="Supprimer le fichier", command=supprimer_fichier, font=("Arial", 12), bg="red", fg="white")
bouton_supprimer.pack(pady=5)

# Initialisation de la liste des fichiers
actualiser_liste_fichiers()

# Lancer la boucle principale
fenetre.mainloop()

# Structure des fichiers dans le dossier :
# - Chaque fichier créé sera dans le dossier courant de l'application.
# - Vous pouvez lire, modifier ou supprimer des fichiers directement via l'interface graphique.
# - Exemple :
#   Dossier actuel :
#   ├── fichier1.txt
#   ├── fichier2.txt
#   ├── gestion_fichiers.py (le script actuel)
