# Il existe 3 différents type de tris :

# Tri par sélection ->
    #   Analyser tous les éléments et repérer le plus petit éléments, le mettre de côté et répéter l'action 

# Tri à bulles (bubble sort) -> 
    #   Compare 2 éléments de manière successive et compare élément gauche plus petit que celui de droite
    #   Si ce n'est pas le cas, on fait une permutation et on continue jusqu'à la fin des éléments
    #   Si sur toutes les comparaisons il y a eu au moins une permutation, on recommence depuis le début jusqu'à ce qu'on fasse un tour sans perm'

# Tri rapide (quick sort) -> 
    #   Choix d'un élément 'pivot', tous les élements plus petits seront à gauche et les plus grand à droite
    #   On réitère en choissisant un autre élement pivot jusqu'à ce que la liste soit complètement trié

# Exercice de tri par sélection sur une liste de numéro : 

l = [3, 5, 1, 2, 9, 7, 4, 10]
l.sort() # -> fait le tri par sélection directement
print(l)

# manuellement ça donne ça :

import random

def generate_random_list(n, min, max):
    l = []
    for i in range(n):
        e = random.randint(min, max)
        l.append(e)
    return l

def selection_sort(l):
    for unsorted_index in range(0, len(l)-1):
        min = l[unsorted_index]
        min_index = unsorted_index
        for i in range(unsorted_index+1, len(l)):
            if l[i] < min:
                min = l[i]
                min_index = i          #   V            m
        l[min_index] = l[unsorted_index]   #  [5, 8, 10, 2, 5]
        l[unsorted_index] = min            #  [1, 8, 10, 2, 5]

l = generate_random_list(10, -10, 10)
print("UNSORTED:", l)

selection_sort(l)

print("SORTED:  ", l)
