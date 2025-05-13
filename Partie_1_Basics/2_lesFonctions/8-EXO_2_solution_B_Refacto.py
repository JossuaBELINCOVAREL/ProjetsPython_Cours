# Fonction qui demande les infos d'une personne et les retourne
def demander_infos_personne(numero):
    print(f"--- Saisie pour la personne n°{numero} ---")
    nom = input("Nom : ")
    prenom = input("Prénom : ")

    # On s'assure que l'âge est bien un nombre
    while True:
        age_str = input("Âge : ")
        try:
            age = int(age_str)
            break
        except:
            print("Erreur : tu dois entrer un nombre entier pour l'âge.")

    ville = input("Ville : ")
    return nom, prenom, age, ville

# Fonction qui affiche les infos d'une personne
def afficher_infos_personne(numero, nom, prenom, age, ville):
    print(f"{prenom} {nom}, âgé de {age} ans, habite à {ville}.")
    print(f"Le prénom contient {len(prenom)} lettres, le nom {len(nom)} lettres, soit {len(prenom) + len(nom)} lettres au total.")
    print("")

# Programme principal
print("Bienvenue dans le gestionnaire de fiches personnelles !")
print("")

# Permet à l’utilisateur de choisir combien de personnes il veut ajouter
while True:
    nb_personnes_str = input("Combien de personnes veux-tu enregistrer ? ")
    try:
        nb_personnes = int(nb_personnes_str)
        break
    except:
        print("Erreur : entre un nombre entier.")

# Boucle principale
for i in range(1, nb_personnes + 1):
    nom, prenom, age, ville = demander_infos_personne(i)
    afficher_infos_personne(i, nom, prenom, age, ville)
