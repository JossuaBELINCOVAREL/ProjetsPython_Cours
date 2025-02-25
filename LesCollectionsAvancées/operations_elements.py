# min, max, in, sum

noms = ["Jean", "Eva", "Sophie", "Martin"]
ages = [21, 32, 4, 56]

print(min(ages))

print(min(noms)) # -> En fonction de l'ordre alphabétique de chaque lettre des prénoms

if "Eva" in noms:
    print("Présent")
else:
    print("Abscent")

if "eva" in noms:
    print("Présent")
else:
    print("Abscent")

print(sum(ages)) # Somme seulement possibles avec des int