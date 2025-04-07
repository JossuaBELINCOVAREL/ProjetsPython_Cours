# Différentes syntaxes pour faire la même chose

nom = "admin" # string
age = 12 # int


# Première méthode d'affichage : f-string (la plus moderne et facile à lire)

print(f"Vous êtes {nom}, vous avez {age} ans") # On insère directement les variables dans la chaîne avec des {}
print()

# Deuxième méthode : concaténation classique (on colle les morceaux ensemble avec +)

print("Vous êtes " + nom + ", vous avez " + str(age) + " ans") # On convertit l'âge en string pour pouvoir le coller
print()

# Troisième méthode : ancienne syntaxe avec % (comme en C ou PHP)

print("Vous êtes %s, vous avez %s ans" % (nom,age)) # %s est un espace réservé pour insérer une variable