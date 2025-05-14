# FONCTIONS : any() et all()

noms = ["Jean", "Eva", "Sophie", "Martin"]

# Ces deux fonctions s’utilisent uniquement avec des listes (ou autres collections) de booléens
# Elles permettent de vérifier si une condition est remplie au moins une fois (any)
# ou TOUT LE TEMPS (all)

# Exemple 1 : any() = "au moins un est vrai"
a = [True, False, True, False]
print(any(a))  # Résultat : True, car il y a au moins un True

# Exemple 2 : aucun élément vrai
b = [False, False]
print(any(b))  # Résultat : False, aucun élément n’est True

# Exemple 3 : all() = "TOUS les éléments sont vrais"
c = [True, True, True]
print(all(c))  # Résultat : True, car tous sont True

# Exemple 4 : tous sauf un
d = [True, True, False]
print(all(d))  # Résultat : False, car un seul False suffit à rendre le résultat False

# APPLICATION : Chercher une lettre dans des noms

# Objectif : Vérifier si AU MOINS un des prénoms contient la lettre "v"

# On crée une liste de booléens, un par prénom
noms_v = [True if "v" in car_nom.lower() else False for car_nom in noms]
print(noms_v)  # Affiche par exemple : [False, True, False, False]

# Solution plus compacte avec any() directement :
noms_v_existe = any([True if "v" in car_nom.lower() else False for car_nom in noms])
print(noms_v_existe)  # Affiche : True, car "Eva" contient un "v"

##############################################
# Exercice : Vérification de données avec any() et all()

# Tu disposes d'une liste d'âges [18, 25, 30, 12, 40].

# Vérifie si au moins une personne est mineure (moins de 18 ans).
# Vérifie si TOUTES les personnes sont majeures (18 ou plus).
# BONUS : Affiche un message adapté selon les résultats.

# Indice : Crée une liste de booléens avec une compréhension de liste.

##############################################

