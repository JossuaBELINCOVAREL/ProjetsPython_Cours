# Fonction qui affiche le statut du candidat selon son âge
def afficher_statut_hero(nom, age):
    print("Nom du candidat :", nom)
    print("Âge :", age)
    if age < 10:
        print("❌ Trop jeune pour rejoindre l'école des héros.")
    elif 10 <= age <= 25:
        print("✅ Admis à l'école des héros !")
    else:
        print("🧠 Recruté comme senior conseiller.")
    print("")  # Ligne vide pour l'affichage

# Fonction qui demande l’âge et vérifie la saisie
def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age = input(nom_personne + ", quel est ton âge ? ")
        try:
            age_int = int(age)
        except:
            print("ERREUR: entre un nombre valide !")
    return age_int

# Nombre de candidats
NB_CANDIDATS = 4

# Boucle pour traiter chaque candidat
for i in range(0, NB_CANDIDATS):
    nom = "candidat" + str(i + 1)  # Génère un nom automatique
    age = demander_age(nom)
    afficher_statut_hero(nom, age)
