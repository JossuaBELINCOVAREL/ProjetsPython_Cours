# Fonction qui demande un prénom
def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Quel est ton prénom ? ")
    return nom

# Fonction qui demande l'âge et vérifie que c'est un nombre
def demander_age():
    age_valide = 0
    while age_valide == 0:
        age = input("Quel est ton âge ? ")
        try:
            age_valide = int(age)
        except:
            print("Erreur : tu dois entrer un nombre.")
    return age_valide

# Fonction qui affiche le message final
def afficher_message(nom, age):
    print("Bonjour " + nom + ", dans 5 ans tu auras " + str(age + 5) + " ans !")

# --- Programme principal ---

nom_utilisateur = demander_nom()
age_utilisateur = demander_age()

afficher_message(nom_utilisateur, age_utilisateur)
