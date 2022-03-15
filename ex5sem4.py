#Écrire un programme prenant l'année de naissance et lui retournant sa génération.
#Vous pouvez utiliser la source suivante: https://www.eurecia.com/blog/generations-x-y-z-sont-elles/

def generation():

    annee = int(input("Entrer votre année de naissance: "))

    if annee >= 1946 and annee <= 1965:
        print ("Votre génération est baby-boomers")

    elif annee >= 1966 and annee <= 1980:
        print ("Votre génération est génération x")

    elif annee >= 1981 and annee <= 2000:
        print ("Votre génération est génération Y")

    elif annee > 2001:
        print ("Votre génération est génération z")

    else:
        print ("Année entrée inférieur a 1946")

        return None

generation()