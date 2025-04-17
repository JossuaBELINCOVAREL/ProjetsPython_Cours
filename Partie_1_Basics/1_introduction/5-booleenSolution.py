# Fonction qui demande le prénom de l'utilisateur
def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Quel est ton prénom ? ")
    return nom

# Fonction qui demande l'âge de l'utilisateur
def demander_age():
    age_int = 0
    while age_int == 0:
        age = input("Quel est ton âge ? ")
        try:
            age_int = int(age)
        except:
            print("Erreur : tu dois entrer un nombre.")
    return age_int

# Fonction qui affiche un message basé sur l'âge de la personne
def afficher_message(nom, age):
    if age < 13:
        print(nom + ", tu es un enfant !")
    elif 13 <= age <= 17:
        print(nom + ", tu es un adolescent !")
    elif 18 <= age <= 65:
        print(nom + ", tu es un adulte !")
    else:
        print(nom + ", tu es un senior !")

# --- Programme principal ---

# Demande le prénom et l'âge
prenom = demander_nom()
age = demander_age()

# Affiche le message en fonction de l'âge
afficher_message(prenom, age)
