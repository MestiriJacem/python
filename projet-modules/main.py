# main.py

# Importation d'un module
import mon_module

# Utilisation des fonctions du module
print("Addition :", mon_module.additionner(5, 3))
print("Multiplication :", mon_module.multiplier(4, 2))
print("Valeur de PI :", mon_module.PI)

# Importation d'un package
import mon_package

# Utilisation des fonctions du package via __init__.py
print(mon_package.saluer("Alice"))
print(mon_package.au_revoir("Alice"))

# Importation de modules spécifiques d'un package
from mon_package.module_a import saluer
from mon_package.module_b import au_revoir

print(saluer("Bob"))
print(au_revoir("Bob"))
