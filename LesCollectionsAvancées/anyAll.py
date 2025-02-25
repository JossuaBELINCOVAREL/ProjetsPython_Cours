noms = ["Jean", "Eva", "Sophie", "Martin"]

# Fonctionne uniquement avec les booléen
# Any = Quelconque, 

a = [True, False, True, False]
print(any(a)) # quand au moins un des éléments rempli un critère True, il affiche True

b = [False, False]
print(any(b))

# All -> Tousles éléments doivent être True 
c = [True, True, True]
print(all(c))

d = [True, True, False]
print(all(d))

# Trouvé si un nom possède un V

noms_v = [True if "v" in car_nom.lower() else False for car_nom in noms]
print(noms_v)

# Possible de faire comme ça aussi avec un any: 
noms_v_existe = any([True if "v" in car_nom.lower() else False for car_nom in noms])
print(noms_v_existe)