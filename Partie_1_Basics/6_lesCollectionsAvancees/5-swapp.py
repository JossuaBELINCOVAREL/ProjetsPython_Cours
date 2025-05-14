# Échanger deux éléments dans une liste (technique de swap)

# On crée une liste de prénoms
noms = ["Jean", "Eva", "Sophie", "Martin"] 

# Affichage de la liste originale
print("Liste originale :", noms)

# ---------------------------------------------
# Objectif : échanger les places de "Eva" et "Martin"
# Position de Eva = index 1
# Position de Martin = index 3

# Grâce à Python, on peut échanger deux valeurs en une ligne :
noms[1], noms[3] = noms[3], noms[1]

# Cela revient à faire :
# temp = noms[1]
# noms[1] = noms[3]
# noms[3] = temp

# Affichage de la liste après le swap
print("Liste après échange :", noms)

##############################################
# Exercice : Échanger des éléments dans une liste

# Tu disposes d'une liste de notes : notes = [10, 12, 14, 16, 18]

# - Affiche la liste de base.
# - Échange la première et la dernière note.
# - Affiche la nouvelle liste.

##############################################

