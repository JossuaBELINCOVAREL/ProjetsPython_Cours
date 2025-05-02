# Methodes Instance / Statiques / Classe(très peu utilisé)

class Personne:
    TYPE = "Humain"
    def __init__(self, nom):
        self.nom = nom 

    # Methode d'instance
    def se_presenter(self):
        print(f"Je m'apelle {self.formater_chaine(self.nom)} - {self.TYPE}")
    
    # Premier caractère en majuscule puis en minuscules
    # Methode statique, ne dépend pas du self
    @staticmethod
    def formater_chaine(a): # On peut appeler cette méthode au sein de la class
        return a[0].upper() + a[1:].lower()
    
    @classmethod
    def methode_de_classe(cls):
        print(f"Methode de classe : {cls.TYPE}") # ici cls c'est comme si on avait écrit Personne

personne1 = Personne("eva")
personne1.se_presenter()
print()

print(Personne.formater_chaine("toTo"))
# Pas besoin de créer une instance vu que c'est une méthode statique

Personne.methode_de_classe()