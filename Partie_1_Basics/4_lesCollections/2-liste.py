# Liste est mutable, on peut rajouter/supprimer des éléments : liste = []

personnes = ["Mélanie", "Jean", "Martin", "Leo"]
nv_personne = "David"

print(personnes)

personnes.append(nv_personne) # -> Ajoute une personne dans la liste
print(personnes)

del personnes[1] # -> Supprime un nom
print(personnes)

print("")

def afficher_personnes(c):
    for i in c:
        print(i)

def modifier_valeur(a):
    a[0] = 10 # -> Modifie la première valeur de la liste 

test = [1, 2, 3, 4, 5]
print(test)
modifier_valeur(test)
print(test)

print("")

afficher_personnes(personnes)