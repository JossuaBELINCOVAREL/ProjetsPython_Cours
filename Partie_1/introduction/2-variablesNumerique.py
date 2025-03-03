# Comprendre les variables numériques

# Premier programme
nom = "admin"
age = 20
age_enfant = "30"
print(type(nom))
print(type(age))
print(type(age_enfant))
print("Je m'appelle " + nom + " et j'ai actuellement " + str(age) + " ans. Mon fils lui à " + age_enfant + " ans.")

# Second programme
age_maintenant = 25
age_prochain = age_maintenant + 1
print("Vous avez actuellemennt " + str(age_maintenant) + " ans, l'année prochaine vous aurez " + str(age_prochain) + " ans.")

# Troisième programme
age_la = input("Quel est ton âge jeune ? ")

try:
    age_pala = int(age_la) + 1
except:
    print("ERREUR: Rentre un nombre !")
else:
    print("Vous avez actuellemennt " + str(age_la) + " ans, l'année prochaine vous aurez " + str(age_pala) + " ans.")