def afficher_notes(liste):
    print("Liste des notes :")
    for note in liste:
        print(note)

def modifier_note(liste):
    # On modifie la dernière note de la liste
    liste[-1] = 20

# Étape 1 : Création de la liste
notes = [12, 15, 9, 18, 13]

# Étape 2 : Ajout d’une nouvelle note saisie par l’utilisateur
nouvelle_note = float(input("Entrez une nouvelle note à ajouter : "))
notes.append(nouvelle_note)

# Étape 3 : Suppression de la première note
del notes[0]

# Étape 4 : Affichage de toutes les notes
afficher_notes(notes)

# Étape 5 : Modification de la dernière note
modifier_note(notes)

# Étape 6 : Affichage après modification
print("\nAprès modification de la dernière note :")
afficher_notes(notes)
