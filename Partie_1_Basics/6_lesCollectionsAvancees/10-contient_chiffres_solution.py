pseudos = ["DarkVador77", "Anakin", "Luke007", "Leia", "Obiwan", "Padmé42"]

print("Pseudos contenant un chiffre :")
for pseudo in pseudos:
    if any([car.isdigit() for car in pseudo]):
        print(pseudo)

print("\n Pseudos SANS chiffre :")
for pseudo in pseudos:
    if not any([car.isdigit() for car in pseudo]):
        print(pseudo)
