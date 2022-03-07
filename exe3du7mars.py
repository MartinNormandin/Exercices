def Naissance(mois, jour):
    if (mois == 1 or mois == 2) or (mois == 3 and jour < 21) or (mois == 12 and jour >=21):
        return "hiver"

    if (mois == 4 or mois == 5) or (mois == 3 and jour >= 21) or (mois == 6 and jour < 21):
        return "printemps"

    elif (mois == 7 or mois == 8) or (mois == 6 and jour >= 21) or (mois == 9 and jour < 21):
        return "été"

    else:
        return "automne"


jour = int(input("entrer votre jour de naissance: "))
mois = int(input("entrer votre mois de naissance en chiffre: "))

print(Naissance(mois,jour))
