# Demander des noms de personnes
# Boucle infini, sortir quand le nom est vide
# Seulement à la fin afficher tous les noms

noms = []

while True:
    nv_nom = input(f"Quel est votre nom : ")
    if nv_nom == "":
        break
    noms.append(nv_nom)

print()
print("Noms des personnes : ")
print(noms)

print()
print("Ordre alphabétiques : ")
noms.sort()
print(noms)