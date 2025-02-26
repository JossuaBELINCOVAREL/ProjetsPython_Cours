# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
nb_personnes = 3
noms_personne = []

for i in range(nb_personnes):
    noms_personne.append(Personne(input(f"nom de la personne {i+1} : ")))

for p in noms_personne:
    p.SePresenter()
