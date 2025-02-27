# Définition de la classe de base Pizza
class Pizza():
    def __init__(self, nom, prix, ingredients, vegetarienne = False):

        # Initialise une instance de Pizza.

        # :param nom: Nom de la pizza (str)
        # :param prix: Prix de la pizza (float)
        # :param ingredients: Liste des ingrédients (list ou tuple)
        # :param vegetarienne: Indique si la pizza est végétarienne (bool, par défaut False)

        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne
    
    def Afficher(self):

        # Affiche les informations de la pizza : nom, prix et liste des ingrédients.
        # Ajoute une mention spéciale si la pizza est végétarienne.

        veg_str = ""
        if self.vegetarienne:
            veg_str = " - VEGETARIENNE"
        print(f"PIZZA {self.nom} : {self.prix} ${veg_str}")
        print(", ".join(self.ingredients))
        print()

# Définition de la classe PizzaPerso qui hérite de Pizza
class PizzaPerso(Pizza):
    # Définition des constantes pour le calcul du prix
    PRIX_BASE = 6 # Prix de base d'une pizza personnalisée
    PRIX_INGREDIENT = 1.2 # Coût supplémentaire par ingrédient
    DERNIER_NUM = 0 # Compteur pour attribuer un numéro unique à chaque pizza personnalisée

    def __init__(self):

        # Initialise une pizza personnalisée en incrémentant un numéro unique,
        # en demandant les ingrédients à l'utilisateur, puis en calculant son prix.

        PizzaPerso.DERNIER_NUM += 1 # Incrémente le numéro de la dernière pizza créée
        self.numero_pizza = PizzaPerso.DERNIER_NUM # Assigne un numéro unique à la pizza
        super().__init__(f"Personalisée {self.numero_pizza}", 0, []) # Initialise la classe mère avec un prix temporaire
        self.demander_ingredients()
        self.calculer_prix()
    
    def demander_ingredients(self):

        # Demande à l'utilisateur d'ajouter des ingrédients à la pizza personnalisée.
        # L'ajout se termine lorsque l'utilisateur appuie sur ENTER sans entrer de texte.

        print()
        print(f"Ingredient pour la pizza personnalisée numéro {self.numero_pizza} : ")
        while True:
            ingredient = input("Ajouter un nouvel ingredient (ENTER pour terminer) : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient) # Ajout de l'ingrédient à la liste
            print(f"Vous avez ajouté {len(self.ingredients)} ingredient : {', '.join(self.ingredients)}")

    def calculer_prix(self):
        self.prix = self.PRIX_BASE + (self.PRIX_INGREDIENT * len(self.ingredients))
        

# Fonction de tri par nombre d'ingrédients --->
    # def tri(e):
    #     return len(e.ingredients) # fonction de tri par nombre d'ingredient

pizzas = [ Pizza("4 fromages", 8.5, ("Brie", "Emmental", "Compté", "Parmesan"), True), 
         Pizza("Margarita", 7, ("Basilique", "Emmental", "Sauce Tomate"), True), 
         Pizza("Reine", 9.5, ("Oeuf", "Emmental", "Jambon", "Champignon", "Olives")), 
         Pizza("Orientale", 11, ("Merguez", "Olives", "Chorizo")),
         PizzaPerso(), # Création d'une pizza personnalisée via l'utilisateur
         PizzaPerso() ]

# Tri des pizzas par nombre d'ingrédients ---> 
    # pizzas.sort(key=tri) # tri par nombre d'ingredients

for p in pizzas:
    p.Afficher()


# Affichage des pizzas dont le prix est supérieur ou égal à 10$ --->
    # for p in pizzas:
    #     if p.prix >= 10:
    #         p.Afficher()

# Affichage des pizzas contenant "Emmental" comme ingrédient --->
    # for p in pizzas:
    #     if "Emmental" in p.ingredients:
    #         p.Afficher()

