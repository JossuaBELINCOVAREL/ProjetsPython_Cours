# Liste de prénoms
prenoms = ["Luc", "Alexandre", "Nina", "Zoé", "Clément"]

# Étape 1 : tri alphabétique
prenoms.sort()
print("Tri alphabétique (in-place) :")
print(prenoms)
print()

# Étape 2 : tri alphabétique sans modifier l’original
prenoms = ["Luc", "Alexandre", "Nina", "Zoé", "Clément"]  # on remet l’original
prenoms_tries = sorted(prenoms)
print("Nouvelle liste triée (sorted) :")
print(prenoms_tries)
print("Liste originale conservée :")
print(prenoms)
print()

# Étape 3 : tri par longueur des prénoms
prenoms.sort(key=lambda p: len(p))
print("Tri par longueur de prénom :")
print(prenoms)
