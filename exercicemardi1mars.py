from cmath import sqrt
import math
#pouquoi laisser une ligne vide après definition de fonction? (ligne 6)

def dms_en_dd(degre,minute,seconde):    

    conversion_minute = minute/60
    conversion_seconde = seconde/3600

    return(degre+conversion_minute+conversion_seconde)

def distance_pole_nord(latitude,longitude): #devrait laisser 2 lignes vide avant la definition d'une fonction.

   return math.sqrt(((86 - latitude)**2) + (172 - longitude)**2)*111.16 #ne pas laisser d'espace pour l'operateur dans une parenthese
#formule un peu longue, devrait déclarer plus de variables dans la fonction

#définir que l'on parle de données dms dans le nom des variables
DEGRE_LATITUDE = 35
MIN_LATITUDE = 39
SEC_LATITUDE = 10.08

DEGRE_LONGITUDE = 139
MIN_LONGITUDE = 50
SEC_LONGITUDE = 21.84

#pouquoi ma_latitude et ma_longitude sont en majuscules?
MA_LATITUDE = (dms_en_dd(DEGRE_LATITUDE,MIN_LATITUDE,SEC_LATITUDE))
MA_LONGITUDE = (dms_en_dd(DEGRE_LONGITUDE,MIN_LONGITUDE,SEC_LONGITUDE))


print(distance_pole_nord(MA_LATITUDE,MA_LONGITUDE))

#commentaire fonction doit toujours aller en haut et different nom de variable (effectué)








