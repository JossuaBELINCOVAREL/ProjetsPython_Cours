# Polymorphisme -> Utiliser la même chose pour des types totalement différents
# Plusieurs types -> même interface, même code

class EtreVivant:
    def afficher_info(self):
        print("Je suis un être vivant")

class Chat(EtreVivant):
    def afficher_info(self):
        print("Je suis un chat")

class Personne(EtreVivant):
    def afficher_info(self):
        print("Je suis une personne")

liste = [EtreVivant(), Chat(), Personne()]

for e in liste:
    e.afficher_info()

# 2e exemple

def additionner(a, b):
    somme = 0
    if isinstance(a, int):
        somme += a
    if isinstance(a, str):
        somme += len(a)
    if isinstance(b, int):
        somme += b
    if isinstance(b, str):
        somme += len(b)
    return somme

print()
print(additionner(10, "aaa"))
print(additionner(10, 3))
    

