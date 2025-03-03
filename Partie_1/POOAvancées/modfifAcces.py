# Public / Private / Protected -> modificateur d'accès
# Pas defaut en Python tout est public, c'est à dire qu'on peut modifier une valeur de la classe dans le code en brut
# Pour private -> rajouter __ devant la variable -> __var
# Pour protected -> rajouter _ devant la variable -> _var

# public : accès depuis l'intérieur et l'extérieur de la classe
# private : accès depuis l'interieur de la classe uniquement
# protected : accès depuis l'interieur de la classe et des classes dérivées 

class Personne:
    def __init__(self, nom):
        # private
        self.__nom = nom 

    def se_presenter(self):
        print(f"Je m'apelle {self.__nom}")

class Etudiant(Personne):
    def se_presenter(self):
        print(f"Je suis étudiant et je m'apelle {self.__nom}")
    

personne1 = Personne("Eva")
personne1.se_presenter()

personne1.__nom = "Antoine" # Ne fonctionne pas car private
personne1.se_presenter()
print()

personne2 = Etudiant("Jean") # Ne fonctionne pas car private, mais possible en le mettant en protected (ou public) car Etudiant est dérivé de Personne 
personne2.se_presenter()