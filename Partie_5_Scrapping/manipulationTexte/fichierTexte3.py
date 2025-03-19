# cas d'erreur (le fichier n'existe pas)

try :
    f = open("fichiernombreExistePAS.txt", "r")

except FileNotFoundError:
    print("Le fichier n'existe pas")

else:
    for line in f:
        print(line, ends="")
    f.close()

"""
Il existe une fonction qui existe sur Python pour savoir si le fichier existe :

import os.path

filename = "fichiernombreExistePAS.txt"

if os.path.exists(filename):
    print("Le fichier existe")
    f = open(filename, "r")
    texte = f.read()
    print(texte)
    f.close()

else:
    print("Le fichier n'existe pas")

"""