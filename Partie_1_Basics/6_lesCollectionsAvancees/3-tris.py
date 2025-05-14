# Tri d'une liste en Python (ordre alphabétique et personnalisé)

# Liste de prénoms
noms = ["Jean", "Eva", "Sophie", "Martin"]

# Affiche la liste originale
print("Liste originale :")
print(noms)
print()

# Trier la liste par ordre alphabétique inversé
# .sort(reverse=True) trie directement la liste, en la modifiant (in-place)
noms.sort(reverse=True)
print("Tri alphabétique inversé :")
print(noms)
print()

# Trier à nouveau dans l’ordre alphabétique normal
noms.sort()
print("Tri alphabétique (A-Z) :")
print(noms)
print()

# Remarque : .sort() modifie la liste **originale**
# Pour garder une copie intacte, il faut utiliser `sorted()` :
# noms_tries = sorted(noms)

# Tri personnalisé selon la longueur du prénom
# Ici on utilise une fonction "lambda" pour dire :
# "Je veux trier selon la taille (len) de chaque nom"
noms.sort(key = lambda nom: len(nom))
print("Tri par longueur de prénom (court -> long) :")
print(noms)
print()

# Même chose mais en ordre décroissant (long -> court)
noms.sort(key = lambda nom: len(nom), reverse=True)
print("Tri par longueur de prénom (long -> court) :")
print(noms)

##############################################
# Exercice : Trier des prénoms

# Tu disposes d'une liste de prénoms.
# Affiche la liste dans l'ordre alphabétique normal.
# Affiche une nouvelle liste triée sans modifier la liste originale.
# Trie la liste originale selon la **longueur des prénoms** (du plus court au plus long).
# Affiche cette liste.

# Indices :
# - Utilise sorted() pour créer une nouvelle liste triée sans altérer l'originale.
# - Utilise une fonction lambda avec `key=` pour le tri par longueur.

##############################################