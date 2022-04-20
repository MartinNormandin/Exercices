#Lire les trois documents: data1.txt, data2.txt et data3.txt

def lecture_fichier():

    fichier1 = open("data1.txt", "r", encoding="utf8")
    contenu1 = fichier1.readlines()
    print(contenu1)
    fichier1.close()

    fichier2 = open("data2.txt", "r", encoding="utf8")
    contenu2 = fichier2.readlines()
    print(contenu2)
    fichier2.close()

    fichier3 = open("data3.txt", "r", encoding="utf8")
    contenu3 = fichier3.readlines()
    print(contenu3)
    fichier3.close()


#lecture_fichier()


#Offrir un menu à l'utilisateur avec les options suivantes: Afficher les statistiques
#Sauvegarder les statistiques, Afficher l'équipe avec les coureurs les plus similaires
#Ajouter une faute à une équipe.

def menu():

    print("Voici votre menu: ")
    print("1.Afficher les statistiques")
    print("2.Sauvegarder les statistiques")
    print("3.Afficher l'equipe avec les coureurs les plus similaires")
    print("4.Ajouter une faute a une equipe")
    choix = int(input("Faire votre choix entre 1, 2, 3 ou 4: "))

    return choix

#menu()


#Vous devez afficher les statistiques suivantes : Équipe ayant le coureur le plus rapide et
#le temps de ce dernier. Temps moyens par équipe présenté en ordre croissant, donc de l'équipe
#la plus rapide à la plus lente. Vous devez y afficher le nom de l'équipe et leur temps de course moyen.


def plus_rapide(equipe_a, equipe_b, equipe_c):

    min(equipe_a)
    min(equipe_b)
    min(equipe_c)

    rapide = ""

    if min(equipe_a) < min(equipe_b) and min(equipe_a) < min(equipe_c):
       rapide = print(f"L'equipe A a le coureur le plus rapide et ce en {min(equipe_a)}")

    elif min(equipe_b) < min(equipe_a) and min(equipe_b) < min(equipe_c):
       rapide = print(f"L'equipe B a le coureur le plus rapide et ce en {min(equipe_b)}")

    else:
        rapide = print(f"L'equipe C a le coureur le plus rapide et ce en {min(equipe_c)}")

    return rapide

def temps_moyen(eq_a, eq_b, eq_c):    
    
    temps_a = sum(eq_a)/nbr_notes 
    temps_b = sum(eq_b)/nbr_notes
    temps_c = sum(eq_c)/nbr_notes

    if temps_a < temps_b and temps_b < temps_c:
        return(f"equipe a avec une moyenne de {temps_a} ensuite equipe b avec {temps_b} et equipe c avec {temps_c}")
    elif temps_a < temps_b and temps_c < temps_b:
        return(f"Equipe a avec une moyenne de {temps_a} ensuite equipe c avec {temps_c} et equipe b avec {temps_b}")

    elif temps_b < temps_a and temps_a < temps_c:
        return(f"Equipe b avec une moyenne de {temps_b} ensuite equipe a avec {temps_a} et equipe c avec {temps_c}")

    elif temps_b < temps_c and temps_c < temps_a:
        return(f"Equipe b avec une moyenne de {temps_b} ensuite equipe c avec {temps_c} et equipe a avec {temps_a}")

    elif temps_c < temps_a and temps_a < temps_b:
        return(f"Equipe c avec une moyenne de {temps_c} ensuite equipe a avec {temps_a} et equipe b avec {temps_b}")

    else:
        return(f"Equipe c avec une moyenne de {temps_c} ensuite equipe b avec {temps_b} et equipe c avec {temps_c}")  

    
    
team_a = [9.25, 9.00, 9.13, 8.5, 10]
team_b = [8.25, 9.00, 9.28, 7.9, 11]
team_c = [7.11, 6.50, 11.12, 8, 13]

nbr_notes = 5
    

stat_1 = plus_rapide(team_a, team_b, team_c)
stat_2 = print(temps_moyen(team_a, team_b, team_c))


#Vous devez sauvegarder les statistiques de l'étape 3 dans un fichier intitulé stats.txt.

def sauvegarde():

    fichier_stats = open("stats.txt", "w", encoding="utf8")
    fichier_stats.write(str(print(stat_1)))
    fichier_stats.write(str(print(stat_2)))
    fichier_stats.close()

sauvegarde()

