# Comprendre les print & les variables

# Premier Programme : Déclaration et affichage de variables
nom_personne = "admin" # Ici, nom_personne est une variable
print(nom_personne) # Ici, on affiche (print) le contenu de la variable

# Affichage d'une phrase avec concaténation de variables
print("Hello World, je m'appelle " + nom_personne + " et j'ai 20ans")
print("Hello World, c'est encore moi, " + nom_personne + "!")

# Second Programme : Affichage structuré de plusieurs variables
# Nous créons une variable pour le prenom et une autre pour le nom
nom = "Dupont"
prenom = "Jean"
print("Prénom :")
print(prenom)
print("Nom :")
print(nom)

# Troisième Programme : Introduction d'une nouvelle variable et affichage formaté
nom = "Dupont"
prenom = "Jean"
profession = "Développeur"
print("Nom : " + nom)
print("Prénom : "  + prenom)
print()
print("Identité : " + prenom + " " + nom + " (" + profession + ")")

# Demander des données à l'utilisateur

# Premier Programme : Demande du nom à l'utilisateur et affichage
nom = input("Quel est ton nom ? ") # On demande au utilisateur de rentrer son nom avec la fonction input et on le stocke dans la variable nom
print("Je m'appelle " + nom + ".")

# Second Programme : Demande du nom et de l'âge à l'utilisateur et affichage
nom_famille = input("Quel est ton nom ? ")
age_famille = input("Quel est ton âge ? ") 
print("Je m'appelle " + nom_famille + " et j'ai " + age_famille + " ans.")

##############################################
# Exercice : Crée ta fiche d'identité personnelle

# Écris un programme en Python qui :
# - Demande à l'utilisateur son prénom, son nom, son âge et sa profession.
# - Affiche ensuite un message structuré de ce type :

'''
Bonjour Jean Dupont !
Tu as 30 ans et tu es Développeur.
'''

##############################################

