import random
import time
import os

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def sequence_inital():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    s = str(f"{a}{b}{c}{d}")
    return s

print("Bienvenue sur le jeu du Simon version suite numérique")
time.sleep(1)
print("Retenez la première séquence")
time.sleep(1)

score = 0

sequence = sequence_inital()
print(sequence)

while True:
    time.sleep(3)
    clear_screen()
    reponse = input("Indiquez le nombre que vous venez de voir : ")

    if reponse == sequence:
        score += 1
        print(f"Bonne réponse, votre score est : {score}")
    else:
        print(f"Mauvaise réponse, la séquence était : {sequence}, votre score final est : {score}")
        exit()

    sequence += str(random.randint(0, 9))
    print(sequence)
