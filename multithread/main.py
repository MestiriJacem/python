# --- INTRODUCTION AU MULTITHREADING EN PYTHON ---

# Le multithreading permet l'exécution de plusieurs threads (sous-processus) en parallèle.
# En Python, le module `threading` permet de créer et gérer des threads.

import threading
import time


# --- Exemple 1 : Thread Simple ---

def dire_bonjour():
    """
    Fonction qui affiche un message toutes les secondes.
    """
    for i in range(5):
        print(f"Bonjour, depuis le thread ! ({i+1}/5)")
        time.sleep(1)  # Pause de 1 seconde


# Création d'un thread
thread1 = threading.Thread(target=dire_bonjour)

# Démarrage du thread
thread1.start()

# Code exécuté en parallèle
for i in range(5):
    print(f"Message principal ({i+1}/5)")
    time.sleep(1)

# Attente de la fin du thread
thread1.join()


# --- Exemple 2 : Utilisation de plusieurs threads ---

def compter(nom, nombre):
    """
    Fonction qui compte jusqu'à un certain nombre.
    """
    for i in range(1, nombre + 1):
        print(f"{nom} compte : {i}")
        time.sleep(0.5)


# Création de plusieurs threads
thread2 = threading.Thread(target=compter, args=("Thread-1", 5))
thread3 = threading.Thread(target=compter, args=("Thread-2", 5))

# Démarrage des threads
thread2.start()
thread3.start()

# Attente de la fin des threads
thread2.join()
thread3.join()


# --- Exemple 3 : Classe Thread Personnalisée ---

class MonThread(threading.Thread):
    """
    Classe personnalisée héritant de threading.Thread.
    """

    def __init__(self, nom, nombre):
        super().__init__()
        self.nom = nom
        self.nombre = nombre

    def run(self):
        """
        Code à exécuter dans le thread.
        """
        for i in range(1, self.nombre + 1):
            print(f"{self.nom} compte : {i}")
            time.sleep(0.5)


# Création d'instances de thread personnalisées
thread4 = MonThread("CustomThread-1", 5)
thread5 = MonThread("CustomThread-2", 5)

# Démarrage des threads
thread4.start()
thread5.start()

# Attente de la fin des threads
thread4.join()
thread5.join()


# --- Exemple 4 : Verrous pour éviter les conflits ---

# Les threads partagent la même mémoire, ce qui peut causer des conflits
# lorsqu'ils accèdent ou modifient les mêmes données.

compteur = 0
verrou = threading.Lock()


def incrementer(nom):
    """
    Incrémente un compteur global en utilisant un verrou pour éviter les conflits.
    """
    global compteur
    for _ in range(5):
        with verrou:  # Acquisition du verrou
            valeur = compteur
            time.sleep(0.1)  # Simulation d'un travail
            compteur = valeur + 1
            print(f"{nom} a incrémenté le compteur à {compteur}")


# Création de threads
thread6 = threading.Thread(target=incrementer, args=("Thread-1",))
thread7 = threading.Thread(target=incrementer, args=("Thread-2",))

# Démarrage des threads
thread6.start()
thread7.start()

# Attente de la fin des threads
thread6.join()
thread7.join()

print(f"Valeur finale du compteur : {compteur}")


# --- Exemple 5 : Pool de threads avec concurrent.futures ---

from concurrent.futures import ThreadPoolExecutor


def travail(nom, duree):
    """
    Simule une tâche longue.
    """
    print(f"{nom} démarre...")
    time.sleep(duree)
    print(f"{nom} terminé après {duree} secondes.")
    return f"{nom} résultat"


# Création d'un pool de threads
with ThreadPoolExecutor(max_workers=3) as executor:
    # Soumission de tâches
    futures = [executor.submit(travail, f"Tâche-{i+1}", i + 1) for i in range(5)]

    # Récupération des résultats
    for future in futures:
        print("Résultat :", future.result())

