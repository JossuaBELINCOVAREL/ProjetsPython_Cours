# Ouvrir un fichier, écrir ou lire puis fermer le fichier

f = open("fichierTexte1.txt", "w") # <- ouverture en ecriture (si le fichier n'existe pas, il est cree)
# open("fichierTexte1.txt", "a") <- ouverture en ajout à la fin du fichier si il existe
l = ["Premiere ligne", "Deuxieme ligne", "Troisieme ligne"]

f.write("Hello world ! \n")
f.write(("\n").join(l))
f.write("\n fin")

f.close()

# open("fichierTexte1.txt", "r") # <- ouverture en lecture

"""
Exercice : créer un fichier qui liste 
"""
nb = open("nombres.txt", "w")

for n in range(10):
    nb.write(str(n+1) + "\n")

nb.close()