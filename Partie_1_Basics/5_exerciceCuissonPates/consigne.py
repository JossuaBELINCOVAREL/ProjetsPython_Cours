"""
Cuisson des pâtes

Vous aimez les pâtes ? Le plus important c'est de respecter la cuisson
3 types de pâtes ont des temps de cuissons différents (pour être al dente bien évidemment...)

Pour cet exercice, vous allez réaliser un programme de type "minuteur" qui permettra d'afficher en temps réel le temps restant de cuisson.

Votre programme proposera 3 options :

- Tagliatelles : 3 minutes
- Fusili : 6 minutes
- Tortelini : 9 minutes

Une fois l'option choisie, votre programme commencera à attendre la durée concernée :

- A chaque seconde, vous afficherez un "." sur une même ligne (afin que l'on voit un effet de progression)
- Toutes les 10 secondes vous irez à la ligne suivante en affichant le temps restant

Exemple:

Temps restant : 2:50..........
Temps restant : 2:40.....

Quand le temps est écoulé, vous afficherez "Cuisson terminée", et votre programme se terminera.

Optionnel : 

- Vous pourrez aussi jouer un son une fois la cuisson terminée

NOTION SUPPLÉMENTAIRES

-> Bloquer le programme pendant 1 seconde :

    import time
    time.sleep(1)

-> Afficher un point sans aller à la ligne :

    print(".", end="", flush=True)

-> Boucler 5 secondes et afficher un "." à chaque seconde :

    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

-> Convertir la durée "d" en secondes, en minutes/secondes :

    d = 100
    min = d//60 # division entière (pas de virgules)
    sec = d-min*60

-> Afficher un nombre avec 2 chiffres complétés par un "0" (si nécessaire) :

    print(f"{min:02d}")

-> Jouer un son

Pour cela vous devrez installer la bibliothèque "beepy" avec la commande :

pip install beepy

Ensuite au niveau du code :

    import beepy
    beepy.beep(sound="ping")

"""