def mult_callback(a, b):
    return a * b

def add_callback(a, b):
    return a + b

def power_callback(a, b):
    return pow(a, b)

def afficher_calcul(n, opertaur_str, operation_callback):
    for i in range(1, 10):
        print(f"{i} {opertaur_str} {n} = {operation_callback(i, n)}")
    
afficher_calcul(2, "x", mult_callback)
print()
afficher_calcul(2, "+", add_callback)
print()
afficher_calcul(2, "^", power_callback)
print()
