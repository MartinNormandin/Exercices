#Créer une liste contenant tous les nombres premiers entre 2 et 20. Ensuite, demander à l'utilisateur d'écrire un nombre entre 2 et 20 (bien vérifier si c'est le cas)
# et vérifier si ce nombre est prime à l'aide de votre liste en affichant le résultat à la console. 2, 3, 5, 7, 11, 13, 17, 19,

def liste():

    liste_nombre_premier = [2, 3, 5, 7, 11, 13, 17, 19]

    nombre = int(input("Enter un nombre entre 1 et 20: "))

    if nombre <= 0 or nombre > 20:
        print("Nombre invalide")

    elif nombre in liste_nombre_premier:
        print("nombre premier")

    else:
        print("Pas un nombre premier")


liste()
        



