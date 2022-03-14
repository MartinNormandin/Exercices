jour_fete = int(input("Entrer votre jour de fete"))
mois_fete = int(input("Entrer votre mois de fete en chiffre"))

if mois_fete <= 3:
    if jour_fete < 21:
        print("Hiver")

if mois_fete <= 6:
    if jour_fete < 21:
        print("printemps")
