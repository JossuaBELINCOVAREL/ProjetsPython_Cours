def afficher_info_personne(nom, age):
    print("Vous vous appelez " + nom + ". Vous avez " + str(age) + " ans, l'année prochaine vous aurez " + str(age + 1) + " ans." )

def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Quel est ton nom ? ")
    return nom

def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age = input(nom_personne + " Quel est ton âge jeune ? ")
        try:
            age_int = int(age)
        except:
            print("ERREUR: Rentre un nombre !")
    return age_int
    
# Demander le nom
nom1 = demander_nom()
nom2 = demander_nom()
# Demander l'âge
age1 = demander_age(nom1)
age2 = demander_age(nom2)
# Afficher les informations
afficher_info_personne(nom1, age1)
afficher_info_personne(nom2, age2)