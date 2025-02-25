noms = ["Jean", "Eva", "Sophie", "Martin"]

print(noms)

# ordre alphabétiques et reverse

noms.sort(reverse=True)
print(noms)

noms.sort() # opération inplace, on à altéré la liste original sans copie
print(noms)
# Avec copie : noms_tries = sorted(noms)

# tri personnalisé par le nombre de caractère (lambda permet d'écrire une fonction directemlent dans le code)

noms.sort(key = lambda noms : len(noms))
print(noms)

# tri personnalisé par le nombre de caractère reverse

noms.sort(key = lambda noms : len(noms), reverse=True)
print(noms)



