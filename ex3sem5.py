#Créer un dictionnaire possédant les cours que vous suivez cette session et leur enseignant respectif. Par exemple:
# Keven Presseau-St-Laurent - Concepts de programmation 1 Ensuite, afficher un menu à la console présentant les 5 cours 
# et offrant à l'utilisateur d'en sélectionner 1. Lorsque l'utilisateur à fait sa sélection, afficher le nom de l'enseignant et le nom du cours à l'écran.

def dictionnaire():

    dict = {"Keven Presseau-St-Laurent" : "Concepts de programmation 1", "Emma Senez Parent": "Logique mathématique", "Jean-Pierre Fiset": "système d'exploitation"}

    print(dict)

    choix = int(input("Choisir un cours (1, 2 ou 3): "))

    if choix == 1:
        print(f"Keven Presseau-st-laurent", dict["Keven Presseau-St-Laurent"])

    elif choix == 2:
        print(f"Emma Senez Parent", dict["Emma Senez Parent"])

    else:
        print(f"Jean-Pierre Fiset", dict["Jean-Pierre Fiset"])

    return choix


#dictionnaire()


#En se basant sur l'exercice 3, créer un fichier bdd.txt fonctionnant comme une base de données
# et remplir le dictionnaire à partir de ce fichier. Pour vous faciliter la tâche, vous pouvez écrire
# les informations de la manière suivante: Nom de cours 1, Nom de prof 1, Nom de cours 2

def fichier():

    mon_fichier = open("bdd.txt", "w")

    mon_fichier.write("Keven Presseau-st-laurent \n")
    mon_fichier.write("Concept de programmation 1 \n")
    mon_fichier.write("Emma Senez Parent \n")
    mon_fichier.write("Logique mathématique \n")
    mon_fichier.write("Jean-Pierre Fiset \n")
    mon_fichier.write("Systeme d'exploitation \n")

    mon_fichier.close()

    mon_fichier = open("bdd.txt", "r")
    contenu = mon_fichier.readlines()
    
    print(f"{contenu[0]}{contenu[1]}{contenu[2]}{contenu[3]}{contenu[4]}{contenu[5]}")


fichier()


    