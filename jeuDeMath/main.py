import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTION = 4

def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 1)
    if o == 1:
        operateur = "*"
    else:
        operateur = "+"

    reponse_str = None
    while reponse_str is None:
        reponse_str = input(f"Calculez {a} {operateur} {b} = ")

        try:
            reponse = int(reponse_str)
        except:
            print("Rentrez un vrai chiffre ou nombre ...")
            reponse_str = None

    reponse = int(reponse_str)
    calcul = a + b
    if o == 1:
        calcul = a * b        
    if reponse == calcul:
        # print("Correct")
        return True
    else:
        # print("Incorrect")
        return False
    
nb_points = 0
for i in range(0, NB_QUESTION):
    print(f"Question n° {i+1} sur {NB_QUESTION}")
    if poser_question():
        print("Correct")
        nb_points += 1
    else:
        print("Incorrect")
    print()

print(f"Vous avez {nb_points} / {NB_QUESTION} points.")
if nb_points == NB_QUESTION:
    print("Excellent ! ")
elif nb_points == 0:
    print("Tu es nul !")
elif nb_points > int(NB_QUESTION / 2):
    print("Tu es au dessus de la moyenne !")
else:
    print("Peux mieux faire !")
