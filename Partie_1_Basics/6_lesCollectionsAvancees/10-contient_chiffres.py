# Vérifier si une chaîne contient des chiffres

# La méthode isdigit() permet de tester si une chaîne contient uniquement des chiffres

print("1".isdigit())       # ✅ True : c’est bien un chiffre
print("a".isdigit())       # ❌ False : ce n’est pas un chiffre
print("12344".isdigit())   # ✅ True : tous les caractères sont des chiffres

print()  # Saut de ligne pour la lisibilité

# Exemple 1 : on teste si un mot contient au moins un chiffre

nom = "toto123"
# Ici, on parcourt chaque caractère du mot, et on vérifie s’il est un chiffre avec isdigit()
# any() retournera True s’il y a AU MOINS un chiffre
contient_chiffre = any([c.isdigit() for c in nom])
print(contient_chiffre)  # True car "1", "2", "3" sont présents dans "toto123"

# Exemple 2 : aucun chiffre

nom = "toto"
contient_chiffre = any([c.isdigit() for c in nom])
print(contient_chiffre)  # False : aucun caractère n’est un chiffre

##############################################
# Exercice : Vérification de numéros dans des pseudos

# Tu as une liste de pseudos de joueurs : ["DarkVador77", "Anakin", "Luke007", "Leia", "Obiwan", "Padmé42"]

# Crée un programme qui affiche uniquement les pseudos qui CONTIENNENT au moins un chiffre.
# Puis, affiche ceux qui ne contiennent PAS de chiffre.

# Indices :
#   - Utilise une boucle `for` pour parcourir les pseudos.
#   - Utilise `any()` avec une compréhension de liste et `isdigit()` comme vu dans le cours.

##############################################
