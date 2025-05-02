def afficher_operations_personnalisees(n, operation_callback):
    for i in range(1, 6):  # De 1 à 5 inclus
        try:
            resultat = operation_callback(i, n)
            print(f"Le résultat de l'opération personnalisée entre {i} et {n} est : {resultat}")
        except Exception as e:
            print(f"Erreur avec les valeurs {i} et {n} : {e}")

print("Soustractions :")
afficher_operations_personnalisees(10, lambda a, b: a - b)

print("\nDivisions :")
afficher_operations_personnalisees(10, lambda a, b: a / b)
