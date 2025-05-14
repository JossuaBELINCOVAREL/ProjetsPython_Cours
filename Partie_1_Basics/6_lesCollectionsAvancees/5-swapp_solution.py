notes = [10, 12, 14, 16, 18]

# Affichage initial
print("Liste de base :", notes)

# Échange de la première (index 0) et la dernière (index -1 ou 4)
notes[0], notes[-1] = notes[-1], notes[0]

# Affichage après échange
print("Liste après échange :", notes)
