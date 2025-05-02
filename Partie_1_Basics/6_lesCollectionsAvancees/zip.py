pizza_nom = ("4 Fromages", "Végétarienne", "Hawai", "Calzone")
pizza_prix = (10.50, 11, 7, 12)

noms_prix = list(zip(pizza_nom, pizza_prix))
print(noms_prix)
print()

'''

for (nom, prix) in noms_prix:
    print(f"{nom} - {prix}$")
    print()

'''

# Possible aussi
for (nom, prix) in zip(pizza_nom, pizza_prix):
    print(f"{nom} - {prix}$")
print()

# Pour l'inverse, en partant d'une liste de tuple

nom, prix = list(zip(*noms_prix))
print(nom, prix)