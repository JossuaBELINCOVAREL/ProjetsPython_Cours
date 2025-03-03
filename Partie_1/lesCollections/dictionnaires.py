# Collection avec des clef -> Valeur
    # personne = {'clef' : 'Valeur', 'clef' : 'Valeur'}
# On peut y ajouter aussi des collection directement

personne = {'nom' : 'Mélanie', 'age' : 25, 'taille' : 1.60}
print(personne)

print(personne['nom'])
print(personne['age'])
print()

personne['nom'] = "Claire" # -> Remplace le nom
print(personne)

personne['poste'] = "développeur" # -> Ajoute une clef/valeur
print(personne)
print()

achat = ("Chocolat", "beurre", "fromage") # -> Ajoute une liste et/ou tuple
personne['achats'] = achat
print(personne)
print()

for i in personne:
    print(i) # Pour itérer sur les clef
    print(personne[i]) # Pour itérer sur les valeurs
