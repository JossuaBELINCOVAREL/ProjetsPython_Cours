personnes = ("Mélanie", "Jean", "Martin", "Leo", "Pierre", "Eva")

for i in personnes:
    print(i)
print()

# afficher les 3 premières personnes
# Les slice fonctionne comme ça : [Start:Stop:Step]
print("3 premiers : ")
for i in personnes[0:3]:
    print(i)
print()

# afficher l'ensemble
print("Ensemble: ")

for i in personnes[:]:
    print(i)
print()


# afficher 1/2
print("1/2 : ")

for i in personnes[::2]:
    print(i)
print()


# afficher à l'inverse
print("Inverse :")

for i in personnes[::-1]:
    print(i)
print()

nom = "Jean"
print(nom[::-1]) # Fonctionne aussi avec les chaines de caractères 