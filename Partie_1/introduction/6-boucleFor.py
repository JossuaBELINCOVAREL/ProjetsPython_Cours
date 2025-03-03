def afficher_info_personne(nom, age):
    print("Vous vous appelez " + nom + ". Vous avez " + str(age) + " ans, l'année prochaine vous aurez " + str(age + 1) + " ans." )
    if age == 17:
        print("Vous êtes encore mineur...")
    elif 12 <= age < 18:
        print("Vous êtes un ado")
    elif age == 1 or age == 2:
        print("Vous êtes un tout petit bébé")
    elif age == 18:
        print("Vous êtes tout juste majeur")
    elif age > 68:
        print("Vous êtes sénior")
    elif age < 10:
        print("Vous êtes un enfant")
    elif age > 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")

def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age = input(nom_personne + " Quel est ton âge jeune ? ")
        try:
            age_int = int(age)
        except:
            print("ERREUR: Rentre un nombre !")
    return age_int

NB_PERSONNE = 3

for i in range(0,NB_PERSONNE):
    nom = "personne" + str(i+1)
    age = demander_age(nom)
    afficher_info_personne(nom, age)