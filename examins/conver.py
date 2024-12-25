# --- Projet 2 : Convertisseur de Températures ---
# Énoncé : Créez un programme qui convertit une température donnée par l'utilisateur.
# L'utilisateur peut choisir entre Celsius -> Fahrenheit ou Fahrenheit -> Celsius.

# Conversion Celsius -> Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Conversion Fahrenheit -> Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Menu pour choisir la conversion
choix = input("Choisissez la conversion :\n1. Celsius vers Fahrenheit\n2. Fahrenheit vers Celsius\nVotre choix : ")

# Réalisation de la conversion en fonction du choix
if choix == "1":
    celsius = float(input("Entrez la température en Celsius : "))
    print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")
elif choix == "2":
    fahrenheit = float(input("Entrez la température en Fahrenheit : "))
    print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit):.2f}°C")
else:
    print("Choix invalide.")
