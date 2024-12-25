from miniprojet.mini import melanger_chaine

lettres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffres = "0123456789"
speciaux = "!@#$%^&*()-_=+[]{};:,.<>?/|"

def melanger_chaine(chaine):
    liste=list(chaine)
    for i in range(len(liste)):
#echanger deux positions :
        j=(i * 7+3)% len(liste)#simple formule pour generer un indice
        liste[i],liste[j]=liste[j], liste[i]
        return ''.join(liste)

def generer_mot_de_passe(longueur,inclure_specieaux):
       caracteres=lettres+chiffres
       if inclure_specieaux:
         caracteres +=speciaux
       caracteres=melanger_chaine(caracteres)
#construction de mot de passe
       mot_de_passe =""
       for i in range(longueur):
           indice=(i*5+2)%len(caracteres)#un autre indice
           mot_de_passe+=caracteres[indice]
           return mot_de_passe
def main():
    print("===generateur de mot de passe")
    try:
        longeur=int(input("entrer la longeur (minimum 6): "))
        if longeur <6 :
            print("Erreur")
            return
        inculre_speciaux = input("inclure des caracteres speciauxx ? (oui/non)").lower=="oui"
        mot_de_passe=generer_mot_de_passe(longeur,inculre_speciaux)
        print(f"Votre mot de passe :{mot_de_passe}")
    except ValueError:
        print("veuillez entrer un nombre valide ")
        main()

