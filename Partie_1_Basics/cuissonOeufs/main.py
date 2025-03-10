import time
import beepy

def temps_fini():
    print("Temps écoulé !!")
    beepy.beep(sound="ping")
    time.sleep(5)
    exit()
    
def cuisson(unit_d):
    d = unit_d
    while d > 0:
        minut = d // 60
        sec = d - minut * 60

        print(f"Temps restant -> {minut:02d} : {sec:02d}", end="", flush=True)
        for i in range(3):
            time.sleep(1)
            print(".", end="", flush=True)
        d -= 10
        print("")

print("Bienvenue sur le programme de cuisson préféré des dev")
# time.sleep(1)
print("Voici les modes de cuissons : ")
# time.sleep(1)
print("1 - Oeuf à la coque : 3 minutes")
print("2 - Oeufs mollets : 6 minutes")
print("3 - Oeufs durs : 9 minutes")
# time.sleep(1)

while True:
    choix_str = input("Choisi le mode de cuisson souhaité : ")

    try:
        choix = int(choix_str)

        if choix == 1:
            cuisson(180)
            temps_fini()

        elif choix == 2:
            cuisson(360)
            temps_fini()

        elif choix == 3:
            cuisson(540)
            temps_fini()

        else:
            print("Rentre un chiffre comprit entre 1 et 3")
            
    except ValueError:
        print("Entre un chiffre...")