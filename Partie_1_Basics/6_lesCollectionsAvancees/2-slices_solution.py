# Liste initiale
eleves = ["Alice", "Benoît", "Chloé", "Damien", "Élise"]

# Étape 1 : copier les 3 premiers prénoms
copie = eleves[:3]  # ["Alice", "Benoît", "Chloé"]

# Étape 2 : modifier la copie
copie[0] = "Zara"

# Étape 3 : afficher les deux listes
print("Liste d'origine :", eleves)
print("Copie modifiée  :", copie)

# Résultat :
# Liste d'origine : ['Alice', 'Benoît', 'Chloé', 'Damien', 'Élise']
# Copie modifiée  : ['Zara', 'Benoît', 'Chloé']
