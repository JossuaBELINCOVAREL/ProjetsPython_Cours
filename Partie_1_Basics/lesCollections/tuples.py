# Tuple est immutable, non modificable : tuple = ("a", "b", "c")

personnes = ("Mélanie", "Jean", "Martin", "Leo")
print(len(personnes))
print(personnes[0])

print("")

for i in personnes:
    print(i)
    print(len(i)) # -> Longeur du nom
    print(i[1]) # -> 2e lettre de chaque nom