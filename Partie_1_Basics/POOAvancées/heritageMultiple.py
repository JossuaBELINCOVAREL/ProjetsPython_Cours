# L'héritage multiple (Multiple-inheritance) -> Existe dans très peu de langages de programmation

class EtreVivant():
    def afficher_infos(self):
        print("Je suis un être vivant")

class Predateur():
    def chasser(self):
        print("MIAAAAAM")

class Lion(EtreVivant, Predateur):
    def afficher_infos(self):
        print("Je suis un lion")
    
class Personne(EtreVivant):
    def afficher_infos(self):
        print("Je suis une personne")

lion = Lion()
lion.afficher_infos()
lion.chasser()