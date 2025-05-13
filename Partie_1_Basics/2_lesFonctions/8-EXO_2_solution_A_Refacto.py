# Fonction qui demande les infos d'une personne
def recuperer_info(numero_personne):
    nom_personne = input(f"Le nom de la personne {numero_personne} est : ")
    prenom_personne = input(f"Le prénom de la personne {numero_personne} est : ")
    age_personne = input(f"L'age de la personne {numero_personne} est : ")
    ville_personne = input(f"La ville de la personne {numero_personne} est : ")
    return nom_personne, prenom_personne, age_personne, ville_personne

# Fonction qui retourne les infos d'une personne
def afficher_info(numero_personne, nom, prenom, age, ville):
    print(f"La personne {numero_personne} est {prenom} {nom}, elle à {age} ans et habite à {ville}.")
    print(f"Son nom comporte {len(nom)} caractères. Son prénom comporte {len(prenom)} caractères.")

def recuperer_afficher_info(numero_personne):
    nom, prenom, age, ville = recuperer_info(numero_personne)
    afficher_info(numero_personne, nom, prenom, age, ville)

# Programme principal
print("Bienvenu !")
print("")

nb_personne = 4
for i in range(nb_personne):
    recuperer_afficher_info(i+1)