def afficher_table_multiplication(n, min, max):
    if min > max:
        print("ERREUR")
        return
    for i in range(min, max):
        resultat = print(f"{i} x {n} = {i * n}")
    

print("Bienvenu !")
print("")

afficher_table_multiplication(6, 1, 10)
    