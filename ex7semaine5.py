#Offrir à l'utilisateur d'entrer un nom de fichier et 5 nombres. Ensuite, créer une liste
#  avec les nombres et imprimer les résultats suivant dans le fichier nommé par l'utilisateur:
#Afficher en ordre croissant
#Afficher en ordre décroissant
#Afficher le maximum
#Afficher le minimum
#Afficher chaque nombre puissance lui-même dans l'ordre initial entré par l'utilisateur. Ex: pow(a, a).
#Afficher la moyenne de la liste
#Afficher la médianne.


def exercice7():

    nom_fichier = input("Entrer un nom de fichier: ")
    nbr1 = int(input("Entrer votre premier nombre : "))
    nbr2 = int(input("Entrer votre deuxième nombre: "))
    nbr3 = int(input("Entrer votre troisième nombre: "))
    nbr4 = int(input("Entrer votre quatrième nombre: "))
    nbr5 = int(input("Entre votre cinquième nombre : "))

    list_nbrs = [nbr1, nbr2, nbr3, nbr4, nbr5]

    print(list_nbrs)


exercice7()

