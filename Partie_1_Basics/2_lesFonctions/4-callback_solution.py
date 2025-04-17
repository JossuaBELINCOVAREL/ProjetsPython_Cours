# Callback functions
def soustraction_callback(a, b):
    return a - b

def division_callback(a, b):
    return a / b

# Fonction principale qui reçoit une fonction en paramètre
def afficher_calcul(n, operateur_str, operation_callback):
    for i in range(1, 10):
        print(f"{i} {operateur_str} {n} = {operation_callback(i, n)}")

# Appels après toutes les définitions
afficher_calcul(10, "-", soustraction_callback)
print()

afficher_calcul(2, "/", division_callback)
print()
