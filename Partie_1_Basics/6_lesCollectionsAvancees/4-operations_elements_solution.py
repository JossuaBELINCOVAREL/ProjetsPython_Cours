notes = [12, 15, 8, 19, 7, 14]

# 1. Note minimale
print("Note minimale :", min(notes))

# 2. Note maximale
print("Note maximale :", max(notes))

# 3. Moyenne
moyenne = sum(notes) / len(notes)
print("Moyenne des notes :", moyenne)

# 4. Vérifier si une note est présente
note_recherchee = int(input("Entre une note à rechercher : "))

if note_recherchee in notes:
    print("✅ La note est présente dans la liste.")
else:
    print("❌ La note n'est pas présente.")
