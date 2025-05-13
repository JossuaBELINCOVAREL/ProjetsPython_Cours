# Étape 1 : Création du dictionnaire
eleve = {
    "prénom": "Lucas",
    "age": 16,
    "classe": "1ère",
    "notes": [14, 12, 17, 15]
}

# Étape 2 : Affichage des infos
print("Informations de l’élève :")
for cle in eleve:
    print(f"{cle} : {eleve[cle]}")
print()

# Étape 3 : Modification du prénom
eleve["prénom"] = "Lucie"

# Étape 4 : Ajout d'une nouvelle note
eleve["notes"].append(18)

# Étape 5 : Calcul de la moyenne
moyenne = sum(eleve["notes"]) / len(eleve["notes"])
print(f"Moyenne des notes : {moyenne:.2f}")
