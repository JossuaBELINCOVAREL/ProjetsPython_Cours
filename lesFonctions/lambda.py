def afficher_calcul(n, opertaur_str, operation_callback):
    for i in range(1, 10):
        print(f"{i} {opertaur_str} {n} = {operation_callback(i, n)}")
    
afficher_calcul(2, "x", lambda a, b : a * b)
print()
afficher_calcul(2, "+", lambda a, b : a + b)
print()
afficher_calcul(2, "^", lambda a, b : pow(a, b))
print()