ages = [18, 25, 30, 12, 40]

# 1. Au moins une personne est mineure ?
mineurs = [age < 18 for age in ages]
print(f"Liste des mineurs : {mineurs}")

au_moins_un_mineur = any(mineurs)
print(f"Au moins un mineur ? {au_moins_un_mineur}")

# 2. Toutes les personnes sont majeures ?
tous_majeurs = all([age >= 18 for age in ages])
print(f"Tous majeurs ? {tous_majeurs}")

# 3. BONUS : Affichage personnalisé
if au_moins_un_mineur:
    print("Attention : il y a des mineurs dans la liste.")
if tous_majeurs:
    print("Tous les individus sont majeurs.")
else:
    print("Tous ne sont pas majeurs.")
