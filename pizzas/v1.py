# Afficher les pizzas
# Afficher la première et la dernière
# Afficher "AUCUNE PIZZA" pour le tuple vide
# Demander à l'utilisateur de rajouter une pizza
# Erreur si pizza existe déja (booleen)

def afficher(collection):

    if collection == ():
        return print("AUCUNE PIZZA")
    
    print(f"----- LISTE DES PIZZAS ({len(collection)}) -----")
    for i in collection:
        print(i)
    print()
    print(f"La première est : {collection[0]}")
    print(f"La dernière est : {collection[-1]}")

def ajouter_pizza(collection):
    nv_pizza = input("Pizza à ajouter : ")
    if pizza_existe(nv_pizza, collection) == False:
        return
    collection.append(nv_pizza)

def pizza_existe(nv, collection):
    for piz in collection:
        if piz == nv:
            print("Cette pizza existe déjà")
            return False

pizzas = ["4 Fromages", "Végétarienne", "Hawai", "Calzone"]
vide = ()

ajouter_pizza(pizzas)

afficher(pizzas)
