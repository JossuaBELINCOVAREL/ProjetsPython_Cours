# INDEX, FIND, COUNT

# On travaille sur une liste de prénoms
noms = ["Jean", "Eva", "Sophie", "Martin"]

# Objectif : Trouver l'index d'un élément dans une liste
element_cherche = "Eva"

# Avant d'utiliser .index(), on vérifie si l'élément est dans la liste
if element_cherche in noms:
    print(noms.index(element_cherche))  # Affiche : 1 (Eva est à l'index 1)
else:
    print("ERREUR, pas dans la collection")


# Exemple avec plusieurs occurrences
noms = ["Jean", "Eva", "Sophie", "Martin", "Eva"]

# .index(valeur, debut) permet de chercher à partir d'une position donnée
# Ici on cherche "Eva" à partir de l’index 3 → donc on trouve la 2ème Eva
if element_cherche in noms:
    print(noms.index(element_cherche, 3))  # Affiche : 4
else:
    print("ERREUR, pas dans la collection")

# COMPTER LE NOMBRE D’OCCURRENCES

nb_occurences = noms.count(element_cherche)  # Compte combien de fois "Eva" apparaît
print(f"nb_occurences : {nb_occurences}")

if nb_occurences > 0:
    index_occurences = 0
    for i in range(nb_occurences):
        # .index(valeur, debut) → utile pour trouver chaque occurrence
        index_occurences = noms.index(element_cherche, index_occurences)
        print(f"{element_cherche} trouvé à l'index : {index_occurences}")
        index_occurences += 1  # On augmente le point de départ pour la prochaine recherche
else:
    print("ERREUR, pas dans la collection")


# .find() sur une CHAÎNE DE CARACTÈRES (et non une liste)

a = "Jean-Martin-Abdel"

# .find() retourne l’index du premier caractère trouvé
i = a.find("Martin")  # Cherche "Martin" dans la chaîne
print(i)  # Affiche : 5, car "Martin" commence au 5e caractère (0-indexé)

##############################################
# Exercice : Analyse de texte et de liste

# On te donne une liste d'aliments : ["pomme", "banane", "poire", "banane", "kiwi", "banane"]

# Ton objectif est de :
#   - Afficher combien de fois "banane" apparaît.
#   - Afficher tous les index où "banane" est présent dans la liste.
#   - Rechercher si "banane" apparaît dans la chaîne de caractères suivante : "J'ai mangé une pomme et une banane."

# Indice : Utilise .count(), .index() et .find() si besoin.

##############################################