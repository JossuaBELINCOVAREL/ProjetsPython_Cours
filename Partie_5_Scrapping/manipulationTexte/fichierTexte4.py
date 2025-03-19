# Utilisation d'une fonction pour gérer les chemins des fichiers

import os.path

# if not os.path.exists("repertoire"):
#    os.mkdir("repertoire")

# Pour supprimer un repertoire, on utilise -> os.rmdir("rep")
# Pour supprimer un fichier, on utilise -> os.remove(filename)


filename = os.path.join("manipulationTexte", "repertoire", "fichierTexte2.txt")
print("filename : ", filename)

if os.path.exists(filename):
    print("Le fichier existe")
    f = open(filename, "r")
    texte = f.read()
    print(texte)
    f.close()

else:
    print("Le fichier n'existe pas")