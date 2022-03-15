#Écrire un programme avec une fonction prenant 2 floats et retournant leur addition soustraction et division. 
# Les résultats des additions doivent avoir au plus 1 chiffre après la virgule,
# la soustraction 2 chiffres après la virgule et la division 3 chiffres après la virgule.

def operations(float1,float2):

    add = f"{float1+float2:.1f}"
    sou = f"{float1-float2:.2f}"
    div = f"{float1/float2:.3f}"

    return add, sou, div

nb1 = float(input("Entrer le premier nombre décimal: "))
nb2 = float(input("Entrer le deuxieme nombre décimal: "))

addition, soustraction, division = operations(nb1,nb2)
print(addition)
print(soustraction)
print(division)

    




