# LONGUEUR DES ZIP
# Permet de regrouper ensemble plusieurs listes, tuples ou itérables en une seule structure. 
# Elle associe les éléments position par position.

# Définition de deux tuples contenant des noms et des âges
noms = ("Jean", "Emilie", "Paul")
ages = (20, 30, 25)

try:
    # Utilisation de zip() avec strict=True pour s'assurer que les séquences ont la même longueur
    noms_et_ages = zip(noms, ages, strict=True)

    # Conversion du zip en liste et affichage du résultat
    print(list(noms_et_ages))

# Capture l'erreur si les séquences ont des longueurs différentes
except ValueError:
    print("ERREUR : nombre d'éléments différents dans le zip")
