# Étape 1 : liste initiale
etudiants = ["Lucas", "Camille", "Nina"]
print("Liste initiale :")
print(etudiants)

# Étape 2 : nouveaux étudiants
nouveaux = ["Adam", "Léa"]

# Étape 3 : ajout avec append (ajoute la liste comme un seul élément)
etudiants_append = etudiants.copy()
etudiants_append.append(nouveaux)
print("Après append :")
print(etudiants_append)

# Étape 3 : ajout avec extend (ajoute les éléments un par un)
etudiants_extend = etudiants.copy()
etudiants_extend.extend(nouveaux)
print("Après extend :")
print(etudiants_extend)

# ou avec +=
etudiants_plus = etudiants.copy()
etudiants_plus += nouveaux
print("Après += :")
print(etudiants_plus)

# Étape 4 : insertion de Inès à l’index 1
etudiants_extend.insert(1, "Inès")
print("Après insertion de Inès :")
print(etudiants_extend)
