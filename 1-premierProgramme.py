# Comprendre les print & les variables

# Premier Programme
nom_personne = "admin"
print(nom_personne)

print("Hello World, je m'appelle " + nom_personne + " et j'ai 20ans")
print("Hello World, c'est encore moi, " + nom_personne + "!")

# Second Programme
nom = "Dupont"
prenom = "Jean"
print("Prénom :")
print(prenom)
print("Nom :")
print(nom)

# Troisième Programme
nom = "Dupont"
prenom = "Jean"
profession = "Développeur"
print("Nom : " + nom)
print("Prénom : "  + prenom)
print()
print("Identité : " + prenom + " " + nom + " (" + profession + ")")

# Demander des données à l'utilisateur

# Premier Programme
nom = input("Quel est ton nom ? ")
print("Je m'appelle " + nom + ".")

# Second Programme
nom_famille = input("Quel est ton nom ? ")
age_famille = input("Quel est ton âge ? ")
print("Je m'appelle " + nom_famille + " et j'ai " + age_famille + " ans.")