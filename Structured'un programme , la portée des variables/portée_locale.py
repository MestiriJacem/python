def addition_locale():
    """Calcule la somme de deux nombres en utilisant des variables locales."""
    nombre1 = 10
    nombre2 = 20
    somme = nombre1 + nombre2
    print(f"La somme de {nombre1} et {nombre2} est {somme} (portée locale)")

if __name__ == "__main__":
    print("--- Portée locale ---")
    addition_locale()