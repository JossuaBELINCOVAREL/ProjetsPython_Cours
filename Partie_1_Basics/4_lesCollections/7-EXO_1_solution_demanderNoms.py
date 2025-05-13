noms = []

while True:
    nv_nom = input(f"Quel est votre nom : ")
    # Si l'utilisateur appuie sur Entrée sans rien taper, on quitte la boucle
    if nv_nom == "":
        break
    # Sinon, on ajoute le nom dans la liste
    noms.append(nv_nom)

print()
print("Noms des personnes : ")
print(noms)

print()
print("Ordre alphabétiques : ")
noms.sort()
print(noms)