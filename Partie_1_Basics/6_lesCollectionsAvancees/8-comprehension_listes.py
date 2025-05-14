# Compréhension de liste (List Comprehension)

noms = ["Jean", "Eva", "Sophie", "Martin", "Abdel"]
print(noms)

# 🎯 Objectif : Créer une nouvelle liste contenant la longueur de chaque nom
longeur_nom = [len(lg_nom) for lg_nom in noms]
# Pour chaque nom dans la liste "noms", on calcule sa longueur avec len()
print(longeur_nom)  # [4, 3, 6, 6, 5]

# 🎯 Avec condition : On garde uniquement les longueurs des noms de moins de 6 lettres
longeur_nom = [len(lg_nom) for lg_nom in noms if len(lg_nom) < 6]
print(longeur_nom)  # [4, 3, 5]

# 🎯 Extraire uniquement les noms qui contiennent la lettre "i"
noms_e = [lg_nom for lg_nom in noms if "i" in lg_nom]
print(noms_e)  # ['Sophie', 'Martin']

# Autres exemples de compréhension de liste

# 🎯 Extraire uniquement les nombres pairs de 0 à 9
a = [i for i in range(10) if (i // 2) * 2 == i]
print(a)  # [0, 2, 4, 6, 8]

# 🎯 Créer une liste contenant True si le nombre est pair, False sinon
b = [True if (i // 2) * 2 == i else False for i in range(10)]
print(b)  # [True, False, True, False, True, False, True, False, True, False]

# 🎯 Créer une liste de tuples (nombre, True/False selon qu’il est pair)
c = [(i, True if (i // 2) * 2 == i else False) for i in range(10)]
print(c)
# [(0, True), (1, False), (2, True), ..., (9, False)]

##############################################
# Exercice : Extraction et transformation avec une compréhension de liste

# On te donne une liste de températures en Celsius : [20, 25, 30, 15, 10, 35, 40]
# Tu dois créer une nouvelle liste contenant uniquement les températures supérieures à 25°C.
# Dans cette même liste, convertis ces températures en Fahrenheit avec la formule : F = C × 1.8 + 32

# Résultat attendu : une liste de températures en Fahrenheit filtrées à partir de celles > 25°C.

##############################################
