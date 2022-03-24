#Créez une fonction demandant à un utilisateur un nombre pair et un nombre impair, une fonction permettant de vérifier que les nombres
#  ne sont pas les deux pairs ou impairs, et affichez la phrase suivante: Votre nombre impair est le x, votre nombre pair est le y et le résultat de leur division est égal à z.
#  Vous ne devez qu'afficher 3 chiffres après le point.

def Nombre():

    nb1 = int(input("Entrer un nombre pair:  "))
    nb2 = int(input("Entrer un nombre impair: "))

    if (nb1 % 2) == 0:
        
        if (nb2 % 2) == 0:
            print("deux nombres pair")

        else:
            print(nb1, nb2, (nb1/nb2))

    else:
        if (nb2 % 2) == 0:
            print("deux nombres impair")

        else:
            print("malgré ordre", nb2, nb1, (nb2/nb1))

     
a = Nombre()



    

    







