import random

def demander_nombre(nb_min, nb_max):
    reponse = 0
    while reponse == 0:
        reponse_str = input(f"Quel est le nombre magique entre {nb_min} et {nb_max} ? ")
        try:
            reponse = int(reponse_str)
        except:
            print("Vous devez rentrer un nombre valide")
        else:
            if reponse < nb_min or reponse > nb_max:
                print(f"Vous devez rentrer un nombre entre {nb_min} et {nb_max} !")
                reponse = 0
    return reponse

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 4

nombre = 0
vies = NB_VIES
while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f"Il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("GG vous avez gagné !")
    elif nombre < NOMBRE_MAGIQUE:
        print("C'est plus grand")
        vies -= 1
    else:
        print("C'est plus petit")
        vies -= 1

if vies == 0:
    print("Vous n'avez plus de vie, vous avez perdu...")
    print(f"Le nombre exact était {NOMBRE_MAGIQUE}")