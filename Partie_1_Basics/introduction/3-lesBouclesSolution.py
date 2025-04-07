# Système de connexion simple avec boucle while

identifiant = ""  # Initialisation
mot_de_passe = ""

# Tant que l'identifiant ou le mot de passe est incorrect
while identifiant != "admin" or mot_de_passe != "1234":
    identifiant = input("Entrez votre identifiant : ")
    mot_de_passe = input("Entrez votre mot de passe : ")

# Si on sort de la boucle, les infos sont correctes
print("Connexion réussie, bienvenue " + identifiant + " !")
