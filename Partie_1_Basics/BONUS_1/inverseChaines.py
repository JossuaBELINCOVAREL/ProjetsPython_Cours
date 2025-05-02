# Inverser une chaine de caractère -> "Bonjour" - "ruojnoB"

# Version 1 avec une boucle : 

def reverse_string(phrase):
    phrase_reverse =""
    for caractere in phrase:
        phrase_reverse = caractere + phrase_reverse
    return phrase_reverse

phrase_a_inverse = "Bonjour toto"
print(phrase_a_inverse)
print(reverse_string(phrase_a_inverse))

# Version 2 avec un Slice : 

print(phrase_a_inverse[::-1]) # ::-1 inverse une chaîne en Python
