noms = ["Jean", "Eva", "Sophie", "Martin"]

# Join -> Coller

noms_join = "-".join(noms)
print(noms_join)
noms_join = " et ".join(noms)
print(noms_join)

# Split -> Séparer

a = "Paul, Marc, Emilie"
a_split = a.split(", ")
print(a_split)

a = "Paul-Marc-Emilie"
a_split = a.split("-")
print(a_split)