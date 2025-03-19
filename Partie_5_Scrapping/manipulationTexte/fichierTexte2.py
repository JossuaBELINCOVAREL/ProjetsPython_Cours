# open("fichierTexte1.txt", "r") # <- ouverture en lecture

f = open("fichierTexte1.txt", "r")

texte = f.read() # <- lire le contenu du fichier (avec readlines on list chaque ligne // avec readline on lit ligne par ligne)
# f.readlines() <- Créer une collection de lignes
print(texte) # <- affiche le contenu du fichier dans la console

f.close()