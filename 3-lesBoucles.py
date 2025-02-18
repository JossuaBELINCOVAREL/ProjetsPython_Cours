# La boucle While

# Premier programme
n = 0
while n < 10:
    print("Valeur de n: " + str(n))
    n = n + 1
print("Fin de la boucle")
print("")

# Second programme
mot_de_passe = ""
while not mot_de_passe == "admin":
    mot_de_passe = input("Entre le mot de passe : ")
print("Bienvenue sur ton compte")
print("")

# Troisième programme
age_prochain = 0
while age_prochain == 0:
    age = input("Quel est ton âge jeune ? ")
    try:
        age_prochain = int(age) + 1
    except:
        print("ERREUR: Rentre un nombre !")
print("Vous avez actuellemennt " + age + " ans, l'année prochaine vous aurez " + str(age_prochain) + " ans.")
print("")

# Quatrième programme
nom = ""
while nom == "":
    nom = input("Quel est ton nom ? ")

age_bientot = 0
while age_bientot == 0:
    age_la = input("Quel est ton âge jeune ? ")
    try:
        age_bientot = int(age_la) + 1
    except:
        print("ERREUR: Rentre un nombre !")
print("Vous vous appelez " + nom+ ".")
print("Vous avez actuellemennt " + age_la + " ans, l'année prochaine vous aurez " + str(age_bientot) + " ans.")