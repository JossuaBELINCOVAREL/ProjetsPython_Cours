noms = ["Jean", "Eva", "Sophie", "Martin"]

# Trouver l'index de "Eva" (donc 1)

element_cherche = "Eva"
if element_cherche in noms:
    print(noms.index(element_cherche))
else:
    print("ERREUR, pas dans la collection")

# Trouver l'index de "Eva" avec une nopuvelle liste ou elle apparait 2 fois

noms = ["Jean", "Eva", "Sophie", "Martin", "Eva"]

element_cherche = "Eva"
if element_cherche in noms:
    print(noms.index(element_cherche, 3)) # ici on passe un index début et fin
else:
    print("ERREUR, pas dans la collection")

# compter le nombre d'occurence dans une liste

element_cherche = "Eva"
nb_occurences = noms.count(element_cherche)
print(f"nb_occurences, {nb_occurences}")

if nb_occurences > 0:
    index_occurences = 0
    for i in range(nb_occurences):
        index_occurences = noms.index(element_cherche, index_occurences)
        print(f"{element_cherche} trouvé à l'index : {index_occurences}")
        index_occurences += 1

else:
    print("ERREUR, pas dans la collection")

# find fonctionne comme index mais sur les chaines de caractère et pas sur les listes

a = "Jean-Martin-Abdel"
i = a.find("Martin")
print(i) # 5 correspond à l'index du caractère