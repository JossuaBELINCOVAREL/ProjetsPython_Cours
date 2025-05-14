# Utilisation des Sets en Python

# Un set (ensemble) est une collection d'éléments uniques et non ordonnés. 
# Contrairement à une liste, les éléments dans un set ne peuvent pas être dupliqués et 
# ne sont pas indexés. On ne peut donc pas accéder à un élément d'un set par son index.

# Exemple :
set_noms = { "Marie", "Paul", "Jean", "Marc", "Emilie", "Marie" }

# Ici, nous avons un set contenant les noms "Marie", "Paul", "Jean", "Marc" et "Emilie".
# Comme les sets ne contiennent que des éléments uniques, "Marie" n'apparaît qu'une seule fois
# bien qu'elle ait été écrite deux fois dans la déclaration.
# On l'affiche ensuite :
print(set_noms)

# Rappel : La non-ordonnabilité d'un set
# Les sets ne conservent pas l'ordre des éléments. 
# Ils ne peuvent pas être indexés comme les listes. Si tu veux accéder à un élément précis, 
# tu dois d'abord convertir le set en liste.

# Exemple :
# noms_sans_doublons = list(set_noms)
# print(noms_sans_doublons[0])

# Si tu veux parcourir tous les éléments du set, tu peux utiliser une boucle `for` :
for s in set_noms:
    print(s)

##############################################
# Exercice : Manipulation de Sets

# Tu as une liste de films : ["Avengers", "Batman", "Superman", "Spiderman", "Batman", "Avengers"]

# Transforme cette liste en un set pour supprimer les doublons.
# Affiche le set résultant.

# Crée un set avec les genres de films : {"Action", "Science-fiction", "Animation", "Action", "Super-héros"}.
#   - Affiche ce set.

# Utilise une boucle `for` pour afficher chaque genre de film.

##############################################
