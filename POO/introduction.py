# POO permet de structurer et d'organiser le code
# Modulaire et évolutif // Facilement réutilisables et réduit les dépendances
# Générique entre les différents langages

# Différence entre programation impérative et POO

# impérative

def afficher_info(nom,age):
    print(f"Bonjours, c'est {nom}, son age est de {age}")

nom1 = "Jean"
age1 = 30

nom2 = "Bob"
age2 = 21

afficher_info(nom1, age1)
afficher_info(nom2, age2)
print()

# POO
'''
Personne : (entité -> class)
    Données : nom, age
    Actions : (méthodes)
        - SePresenter()
        - DemanderNom()

'''
# --- DEFINITIONS ---
class Personne:
    def __init__(self, nom: str, age: int): # Ici c'est le constructeur
        self.nom = nom # Ici on stock dans notre self (un gros sac à dos) le nom // Création d'une variable d'instance : nom
        self.age = age
        print(f"Constructeur personne {nom}")

    def SePresenter(self):
        print(f"Bonjours je m'apelle {self.nom}, j'ai {self.age} ans")

    def AutreFonction():
        print("Autre Fonction")

# --- UTILISATION ---
personne1 = Personne("Eva", 30) # Création d'une personne
personne2 = Personne("Paul", 25)

personne1.SePresenter() # Ici ça correspond à : Personne.SePresenter(personne1) // methode d'instance car on instance sur un objet une méthode
personne2.SePresenter()

print(f"Le nom 1 est {personne1.nom}")

Personne.AutreFonction() # Méthode de classe
