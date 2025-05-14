# Append / Extend / += / Insert sur les listes

# On commence avec une liste de noms
noms = ["Jean", "Eva", "Sophie", "Martin"]

# Une autre liste avec des noms supplémentaires
nom_supplementaires = ["Tom", "Bobby"]

# .append() ajoute UN SEUL élément à la fin de la liste
# Ici, on ajoute toute la liste `nom_supplementaires` comme un seul bloc
noms.append(nom_supplementaires)
print("Avec append :")
print(noms)
# Résultat : ["Jean", "Eva", "Sophie", "Martin", ["Tom", "Bobby"]]

# .extend() ajoute chaque élément d’une autre liste un par un
# On ajoute ici "Tom" et "Bobby" séparément à la fin
noms.extend(nom_supplementaires)
print("Avec extend :")
print(noms)

# += fonctionne comme extend, il ajoute les éléments un par un
# C’est équivalent à : noms = noms + nom_supplementaires
noms += nom_supplementaires
print("Avec += :")
print(noms)

# .insert() permet d’ajouter un élément à un endroit spécifique dans la liste
# Ici, on insère "Joss" entre "Jean" et "Eva", donc à l’index 1
noms.insert(1, "Joss")
print("Avec insert :")
print(noms)

##############################################
# Exercice : Gestion d’une liste d’étudiants

# Tu es chargé(e) de gérer la liste des étudiants d’une classe.

# - Crée une liste avec 3 prénoms d’étudiants
# - Crée une seconde liste avec 2 nouveaux étudiants

# Ajoute la seconde liste à la première :
#  - d’abord avec append
#  - ensuite avec extend (ou +=)

# - Insère un élève "Inès" entre le 1er et le 2ème étudiant de la liste
# - Affiche la liste finale à chaque étape pour observer les différences

##############################################
