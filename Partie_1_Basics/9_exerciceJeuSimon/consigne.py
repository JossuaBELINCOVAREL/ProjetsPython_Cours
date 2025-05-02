"""

Pour cet exercice vous allez réaliser un jeu de mémoire (aussi connu sous le nom du "Simon").


- Le principe :


Vous allez demander à l'utilisateur de mémoriser une séquence de chiffres de plus en plus longue.


La séquence sera aléatoire, et commencera avec 4 chiffres. L'utilisateur à 3 secondes pour la mémoriser.


Si il donne la bonne réponse, on rajoute un nouveau chiffre à la suite de la séquence on la redemande à l'utilisateur... et ainsi de suite, jusqu'à ce que l'utilisateur se trompe.


(Regardez la vidéo d'instructions ci-dessus)


- Remarques :


La séquence sera affichée pendant 3 secondes, puis effacée de l'écran pour que l'utilisateur donne sa réponse.


-------

Pour effacer l'écran, vous allez copier dans votre code cette fonction :


    import os
     
    def clear_screen():
        if(os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')


⚠️ Attention : Ceci ne fonctionne pas dans le terminal de Pycharm

- Solution 1 :

Dans Pycharm :

Run > Edit Configurations

Puis dans la fenêtre Run/Debug configuration qui s'ouvre, cocher la ligne Emulate terminal in ouput console. Puis OK et relancer l'exécution du programme. Il y a de fortes chances que le problème vienne de là.

- Solution 2 :

Lancer le programme à partir de Visual Studio Code (ou bien directement à partir d'un terminal avec "python main.py")


-------

Pour bloquer l'execution de votre programme pendant "x" secondes, vous utiliserez la fonction :


    import time
    time.sleep(x)


Pour générer un chiffre aléatoire entre 0 et 9, vous utiliserez :


    import random
    n = random.randint(0, 9)


Vous devez aussi gérer un score, initialement égal à 0, et qui s'incrémente de 1 à chaque bonne réponse.


Quand l'utilisateur donne une mauvaise réponse, le programme s'arrête directement et affiche (exemple) :


    Mauvaise réponse, la séquence était : 77686
    Votre score final : 1



- Voici le déroulement exact de votre programme :


0 - Générer une chaine de caractère qui contient 4 chiffres aléatoires, c'est votre séquence initiale.

1 - Ajouter un nouveau nombre aléatoire à la fin de votre séquence

2 - Nettoyer l'écran et affichez "Retenez la séquence" pendant 1 seconde

3 - Afficher la séquence à mémoriser pendant 3 secondes

4 - Nettoyer n'écran et demander la réponse à l'utilisateur

5 - Si la réponse est bonne, afficher pendant 1 seconde "Bonne réponse, votre score est : xxx", puis reboucler à l'étape 1

5bis - Si la réponse n'est pas bonne, sortir du programme et afficher : "Mauvaise réponse, la séquence était : xxxx, votre score final : xxxx"

"""