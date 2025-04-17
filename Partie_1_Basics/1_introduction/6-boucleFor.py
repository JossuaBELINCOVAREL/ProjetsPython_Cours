# Utilisation de la boucle For

# Fonction qui affiche les informations en fonction de l'âge de la personne
def afficher_info_personne(nom, age): # Affiche le nom et l'âge actuel de la personne, ainsi que son âge l'année prochaine
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

# Fonction qui demande l'âge d'une personne et s'assure que c'est un nombre valide
def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age = input(nom_personne + " Quel est ton âge jeune ? ")
        try:
            age_int = int(age)
        except:
            print("ERREUR: Rentre un nombre !")
    return age_int # Retourne l'âge valide une fois qu'il est correctement converti en entier

# Variable NB_PERSONNE qui détermine combien de personnes on va traiter
NB_PERSONNE = 3 # On décide de traiter les informations de 3 personnes

# Boucle pour traiter les informations de chaque personne
for i in range(0,NB_PERSONNE): # On répète le processus pour chaque personne
    nom = "personne" + str(i+1) # Crée un nom dynamique pour chaque personne (personne1, personne2, personne3)
    age = demander_age(nom)
    afficher_info_personne(nom, age) # Affiche les informations de la personne

##############################################
# Exercice : Le Test d'Admission à l'École des Héros

# Écris un programme en Python qui :
# - Demande l’âge de 4 candidats (appelés automatiquement candidat1, candidat2, etc.).
# - Pour chaque candidat, le programme devra :
    # Afficher son nom (candidatX)
    # Dire s’il est trop jeune, admis, ou senior conseiller, selon son âge :
        # Moins de 10 ans → ❌ Trop jeune
        # Entre 10 et 25 ans → ✅ Admis à l’école des héros
        # Plus de 25 ans → 🧠 Recruté comme senior conseiller
# - Utilise une boucle for pour ne pas répéter le code manuellement.

##############################################