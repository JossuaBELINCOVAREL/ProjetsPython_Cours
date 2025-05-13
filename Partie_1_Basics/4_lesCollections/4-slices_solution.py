# Étape 1 : Phrase de départ
phrase = "Python est un langage amusant et puissant"

# Étape 2 : Afficher les 6 premiers caractères
print("6 premiers caractères :")
print(phrase[:6])
print()

# Étape 3 : Afficher uniquement le mot "langage"
# Ce mot commence à l’indice 14 (en comptant bien les espaces)
print("Mot 'langage' :")
print(phrase[14:21])
print()

# Étape 4 : Afficher la phrase à l’envers
print("Phrase inversée :")
print(phrase[::-1])
print()

# Étape 5 : Afficher un mot sur deux
print("Un mot sur deux :")
mots = phrase.split()       # Découpe la phrase en liste de mots
mots_1_sur_2 = mots[::2]    # Slice avec un pas de 2
for mot in mots_1_sur_2:
    print(mot)
