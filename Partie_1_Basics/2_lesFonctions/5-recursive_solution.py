def somme_pairs(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        return n + somme_pairs(n - 2)
    else:
        return somme_pairs(n - 1)

def demander_limite():
    reponse = input("Entrez une limite entière positive : ")
    try:
        val = int(reponse)
        if val < 0:
            print("ERREUR : Veuillez entrer un nombre positif.")
            return demander_limite()
        return val
    except:
        print("ERREUR : Ce n’est pas un nombre valide.")
        return demander_limite()

limite = demander_limite()
resultat = somme_pairs(limite)
print(f"La somme des nombres pairs jusqu'à {limite} est : {resultat}")