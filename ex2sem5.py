#Créer une liste de 5 éléments : [1, 2, 5, 3, 4]. Ensuite, créer deux copies de cette liste, une copie en surface et une
# copie profonde intitulée respectivement surface et profonde. Finalement, demander à l'utilisateur d'entrer un mot, modifier le 3e élément
# de la liste «surface» et «profonde» et imprimer les trois listes à la console.

import copy

def liste():

    liste1 = [1, 2, 5, 3, 4]

    surface = liste1[:]

    profonde = copy.deepcopy(liste1)

    mot = input("Enter un mot: ")

    surface.insert(2, mot)

    profonde.insert(2, mot)

    return liste1, surface, profonde


print(liste())