class Pizza():
    def __init__(self, nom, prix, ingredients, vegetarienne = False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne
    
    def Afficher(self):
        veg_str = ""
        if self.vegetarienne:
            veg_str = " - VEGETARIENNE"
        print(f"PIZZA {self.nom} : {self.prix} ${veg_str}")
        print(", ".join(self.ingredients))
        print()

class PizzaPerso(Pizza):
    PRIX_BASE = 6
    PRIX_INGREDIENT = 1.2
    DERNIER_NUM = 0

    def __init__(self):
        PizzaPerso.DERNIER_NUM += 1
        self.numero_pizza = PizzaPerso.DERNIER_NUM
        super().__init__(f"Personalisée {self.numero_pizza}", 0, [])
        self.demander_ingredients()
        self.calculer_prix()
    
    def demander_ingredients(self):
        print()
        print(f"Ingredient pour la pizza personnalisée numéro {self.numero_pizza} : ")
        while True:
            ingredient = input("Ajouter un nouvel ingredient (ENTER pour terminer) : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez ajouté {len(self.ingredients)} ingredient : {', '.join(self.ingredients)}")

    def calculer_prix(self):
        self.prix = self.PRIX_BASE + (self.PRIX_INGREDIENT * len(self.ingredients))
        

# def tri(e):
#     return len(e.ingredients) # fonction de tri par nombre d'ingredient

pizzas = [ Pizza("4 fromages", 8.5, ("Brie", "Emmental", "Compté", "Parmesan"), True), 
         Pizza("Margarita", 7, ("Basilique", "Emmental", "Sauce Tomate"), True), 
         Pizza("Reine", 9.5, ("Oeuf", "Emmental", "Jambon", "Champignon", "Olives")), 
         Pizza("Orientale", 11, ("Merguez", "Olives", "Chorizo")),
         PizzaPerso(),
         PizzaPerso() ]

# pizzas.sort(key=tri) # tri par nombre d'ingredients

for p in pizzas:
    p.Afficher()

# for p in pizzas:
#     if p.prix >= 10:
#         p.Afficher()

# for p in pizzas:
#     if "Emmental" in p.ingredients:
#         p.Afficher()

