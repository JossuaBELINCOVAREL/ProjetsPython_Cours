# ANNOTATIONS
# types de parametres / code de retour de fonctions
# Permet d'améliorer la documentation du code
# Annotated[]

from typing import Annotated

def imc(poids: Annotated[float, "kg"], taille: Annotated[float, "mètres"]) -> float:
    return poids / (taille * taille)


print(imc(67.5, 1.75))
print(imc.__annotations__)
