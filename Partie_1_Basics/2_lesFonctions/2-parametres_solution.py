# Fonction qui salue l'utilisateur si un prénom est fourni
def saluer_utilisateur(prenom=""):
    if prenom == "":
        print("Erreur : prénom manquant")
        return
    print("Bonjour " + prenom + "!")

# Appels de la fonction avec différents prénoms
saluer_utilisateur("Alice")
saluer_utilisateur("")
saluer_utilisateur("Lucas")
