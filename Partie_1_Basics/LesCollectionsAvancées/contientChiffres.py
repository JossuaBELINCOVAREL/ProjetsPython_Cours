# Tester si une chaine contient des chiffres
# any / isdigit

print("1".isdigit())
print("a".isdigit())
print("12344".isdigit())
print()

nom = "toto123"
contient_chiffre = any([c.isdigit() for c in nom])
print(contient_chiffre)

nom = "toto"
contient_chiffre = any([c.isdigit() for c in nom])
print(contient_chiffre)

# Ici, True dit que Oui (Chiffre dans le nom) et False dit que non (pas de chiffre dans le nom)