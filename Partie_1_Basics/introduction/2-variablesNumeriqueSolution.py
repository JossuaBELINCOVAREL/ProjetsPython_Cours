# On demande l'âge à l'utilisateur
age_utilisateur = input("Quel est ton âge ? ")

try:
    # On essaye de convertir l'entrée en nombre et on calcule l'âge de l'année dernière
    age_annee_derniere = int(age_utilisateur) - 1
except:
    # Si l'utilisateur n'a pas entré un nombre, on affiche une erreur
    print("Erreur : Merci d'entrer un nombre valide pour ton âge.")
else:
    # Si tout est bon, on affiche le résultat
    print("Tu as " + str(age_utilisateur) + " ans aujourd'hui, l'année dernière tu avais " + str(age_annee_derniere) + " ans !")
