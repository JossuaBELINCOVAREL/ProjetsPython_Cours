noms = ["Jean", "Eva", "Sophie", "Martin", "Abdel"]
print(noms)

# Créer une liste qui va contenir l'ensemble des longueurs de caractères pour chaque noms
longeur_nom = [len(lg_nom) for lg_nom in noms]
print(longeur_nom)

# Rajout d'une condition, si la longueur est inférieur à 6 on la rejoute
longeur_nom = [len(lg_nom) for lg_nom in noms if len(lg_nom) < 6]
print(longeur_nom)

# Seulement les noms avec un i
noms_e = [lg_nom for lg_nom in noms if "i" in lg_nom]
print(noms_e)

# Création sans liste avant en affichant seuelemnt les pairs

a = [i for i in range(10) if (i//2)*2 == i]
print(a)

# Impair False et paire True
b = [True if (i//2)*2 == i else False for i in range(10)]
print(b)

# Création d'une liste de tuple
c = [(i, True if (i//2)*2 == i else False) for i in range(10)]
print(c)