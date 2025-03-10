def obtenir_info():
    return "Mélanie", 37, 1.60

infos = obtenir_info()
print(infos)
print()

print("nom : " + infos[0])
print("age : " + str(infos[1]))
print("taille : " + str(infos[2]))
print()

nom, age, taille = obtenir_info()
print(f"Informations : Son nom est {nom}, son age est de {age} ans et elle mesure {taille}")
print()

def afficher_informations(nom, age, taille):
    print(f"Informations : Son nom est {nom}, son age est de {age} ans et elle mesure {taille}")

nom, age, taille = obtenir_info()
afficher_informations(nom, age, taille) 
afficher_informations(*infos) # -> Ici l'étoile (*) permet de récupérer les arguments : ici c'est comme si : afficher_informations(infos[0], infos[1], infos[2])

print(infos)
print(*infos)
