# Append / Extend / += / Insert

noms = ["Jean", "Eva", "Sophie", "Martin"]

nom_supplementaires = ["Tom", "Bobby"]

# Ajoute l'élement global :

noms.append(nom_supplementaires)
print(noms)

# Ajoute élement par élément :

noms.extend(nom_supplementaires)
print(noms)

noms += nom_supplementaires
# similaire à : noms = noms + noms_supplementaires
print(noms)

# Ajoute un élement à un endroit entre "Jean" et "Eva":
noms.insert(1, "Joss")
print(noms)

