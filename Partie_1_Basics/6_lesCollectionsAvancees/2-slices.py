# Utilisation du slicing (tranchage) sur les listes

# Une liste de noms d'exemple
noms = ["Jean", "Eva", "Sophie", "Martin"]

# Slicing : noms[start:stop]
# Cela permet de sélectionner une partie de la liste

# Affiche les éléments de l'index 0 à 2 (3 non inclus)
print(noms[0:3])  # ["Jean", "Eva", "Sophie"]

# Équivalent : si start = 0, on peut l’omettre
print(noms[:3])   # ["Jean", "Eva", "Sophie"]

# noms[:] crée une **copie complète** de la liste
print(noms[:])    # ["Jean", "Eva", "Sophie", "Martin"]

# Attention à la différence :
# - noms[:] crée une **nouvelle liste** indépendante
# - noms (sans les crochets) fait juste référence à la liste d’origine

# Exemple pour montrer la différence entre copier et référencer

# On crée une copie de la liste `noms`
slice_noms = noms[:]

# On modifie la première valeur de la copie
slice_noms[0] = "Abdul"

# La copie a bien été modifiée
print("Liste copiée modifiée :", slice_noms)

# Mais l’originale n’a pas changé
print("Liste originale :      ", noms)

# ⚠️ Si on avait fait : slice_noms = noms (sans [:])
# alors les deux listes auraient pointé vers la même zone mémoire,
# et le changement aurait affecté les deux.

##############################################
# Exercice : Travailler avec les slices

# Tu as une liste de prénoms d’élèves :
# - Copie les 3 premiers dans une nouvelle liste.
# - Modifie le premier prénom de la nouvelle liste.
# - Vérifie ensuite que la liste d'origine n’a pas été modifiée.
# - Affiche les deux listes pour comparaison.

##############################################
