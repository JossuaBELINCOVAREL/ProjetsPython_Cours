# Tuple contenant plusieurs prénoms
personnes = ("Mélanie", "Jean", "Abdel", "Julie", "Pierre", "Eva")

# Affiche toutes les personnes une par une
for i in personnes:
    print(i)
print()

# -------------------------------
# Les SLICES permettent de récupérer une partie d'une séquence (liste, tuple, chaîne de caractères, etc.)
# La syntaxe est : sequence[DEBUT:FIN:PAS]
# - DEBUT : indice de départ (inclus)
# - FIN : indice d'arrêt (exclu)
# - PAS : intervalle entre les éléments (optionnel)
# -------------------------------

# Afficher les 3 premières personnes du tuple (indice 0 à 2)
print("3 premiers : ")
for i in personnes[0:3]:
    print(i)
print()

# Afficher tout le contenu du tuple
print("Ensemble: ")
for i in personnes[:]:  # Pas de début ni de fin : on prend tout
    print(i)
print()

# Afficher 1 personne sur 2
print("1/2 : ")
for i in personnes[::2]:  # On saute une personne sur deux (pas = 2)
    print(i)
print()

# Afficher la liste à l'envers
print("Inverse :")
for i in personnes[::-1]:  # Pas négatif = lecture en sens inverse
    print(i)
print()

# Les slices fonctionnent aussi sur les chaînes de caractères !
nom = "Jean"
print(nom[::-1])  # Affiche "naeJ", c'est-à-dire le prénom à l'envers

##############################################
# Exercice : Manipulation d'une phrase avec des slices

# Écrivez un programme qui fait les étapes suivantes :

# Créez une variable appelée `phrase` contenant la phrase suivante : "Python est un langage amusant et puissant"

# - Affichez uniquement les 6 premiers caractères
# - Affichez le mot "langage" à l’aide des slices
# - Affichez toute la phrase à l’envers
# - Affichez un mot sur deux en vous basant sur les espaces

# Indice : utilisez la méthode .split() pour transformer la phrase en liste de mots)

##############################################