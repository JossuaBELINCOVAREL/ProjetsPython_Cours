noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

# V1 avec for et len
somme = 0
for nom in noms:
    somme += len(nom)
print(f"Le nombre total de caractères : {somme}")

# V2 Completion de liste + sum
longeur_noms = [len(nom) for nom in noms]
print("Nombre total de caractères:", sum(longeur_noms))

# V3 - Join / len
print("Nombre total de caractères:", len("".join(noms)))
