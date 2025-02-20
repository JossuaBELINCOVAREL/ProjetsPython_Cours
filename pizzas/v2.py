# Retirer la fonction pizza_existe
# Enlever la sensibilité à la casse (Majuscule & Minuscule)
# Trier par pizza en fonction de leur ordre alphabétique
# Afficher de manière optionnels les 3 premières pizzas

def afficher(collection, number=0):

    if collection == ():
        return print("AUCUNE PIZZA")
    
    collection.sort()
    
    print(f"----- LISTE DES PIZZAS ({len(collection)}) -----")

    if number != 0:
        for i in collection[0:number]:
            print(i)
    else:
        for i in collection:
            print(i)

    print()
    print(f"La première est : {collection[0]}")
    print(f"La dernière est : {collection[-1]}")

def ajouter_pizza(collection):
    nv_pizza = input("Pizza à ajouter : ")
    if nv_pizza.lower() in collection:
        print("CETTE PIZZA EXISTE DEJA")
    else:
        collection.append(nv_pizza)


pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]
vide = ()

ajouter_pizza(pizzas)

afficher(pizzas, 3)