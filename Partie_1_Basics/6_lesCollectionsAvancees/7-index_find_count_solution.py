aliments = ["pomme", "banane", "poire", "banane", "kiwi", "banane"]

# a) Nombre d'apparitions de "banane"
nb_bananes = aliments.count("banane")
print(f"Nombre de bananes : {nb_bananes}")

# b) Index de chaque "banane"
if nb_bananes > 0:
    debut = 0
    for i in range(nb_bananes):
        index_banane = aliments.index("banane", debut)
        print(f"'banane' trouvée à l'index : {index_banane}")
        debut = index_banane + 1
else:
    print("Aucune 'banane' trouvée.")

# c) Recherche dans une chaîne de caractères
phrase = "J'ai mangé une pomme et une banane."
position = phrase.find("banane")
if position != -1:
    print(f"'banane' trouvée dans la phrase à l'index {position}")
else:
    print("'banane' n'est pas dans la phrase.")
