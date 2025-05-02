"""
📘 Exercice : Table de multiplication personnalisée

🎯 Objectif :
Créer une fonction Python qui affiche une table de multiplication en fonction de trois paramètres :
- Le nombre dont on souhaite la table (ex : 5)
- Le minimum de la plage de multiplication (ex : 1)
- Le maximum de la plage de multiplication (ex : 10)

✅ Consignes :

1. Crée une fonction appelée `afficher_table_multiplication` qui prend 3 paramètres :
    - `n` : le nombre pour lequel on veut afficher la table
    - `min` : la valeur minimale de départ
    - `max` : la valeur maximale de fin

2. La fonction doit afficher la table de multiplication comme ceci (exemple pour `n = 5`, `min = 1`, `max = 10`) :
    1 x 5 = 5
    2 x 5 = 10
    3 x 5 = 15
    ...
    9 x 5 = 45

    ⚠️ Attention : la boucle s'arrête avant `max`, comme souvent avec les boucles `for`.

3. Si la valeur de `min` est supérieure à `max`, affichez "ERREUR" et quittez la fonction immédiatement avec `return`.

4. Ensuite, affichez un petit message de bienvenue dans le programme principal, puis appelez la fonction avec ces valeurs :
    afficher_table_multiplication(5, 1, 10)

ℹ️ Indices :

- Utilise une boucle `for` avec `range(min, max)`
- Pour afficher un résultat comme `3 x 5 = 15`, utilise les f-strings :  
    print(f"{i} x {n} = {i * n}")

- Pour vérifier si `min > max`, utilise une condition `if`

🎁 Bonus (optionnel) :
- Demander à l'utilisateur de saisir lui-même les 3 valeurs via input()
- Afficher un message clair si les entrées ne sont pas valides (ex : un texte au lieu d’un chiffre)

Bonne chance !
"""
