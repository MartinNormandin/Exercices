#Écrire un programme offrant un menu à un utilisateur avec 3 choix et lui affichant la phrase suivante une fois sélectionné:
#1. Bonjour
#2. Au revoir
#3. À plus tard

def choix():

    print("Choix #1 = Bonjour")
    print("Choix #2 = Au revoir")
    print("Choix #3 = À plus tard")
    user = int(input("Veuillez choisir le numéro désiré: "))

    phrase = ""

    if user == 1:
        phrase = "Bonjour"

    if user == 2:
        phrase = "Au revoir"

    if user == 3:
        phrase = "A plus tard"

    return phrase    

print(choix())




