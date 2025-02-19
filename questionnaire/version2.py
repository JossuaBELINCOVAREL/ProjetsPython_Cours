def question_reponse(numero_question, pays, a, b, c, d, bonne_reponse):
    print(f"Question {numero_question} : Quelle est la capitale de la {pays} ? ")
    print(f"(a) - {a}")
    print(f"(b) - {b}")
    print(f"(c) - {c}")
    print(f"(d) - {d}")
    reponse = input("Votre réponse : ")
    resultat_reponse(reponse, bonne_reponse)

def resultat_reponse(reponse, bonne_reponse):
    global score
    if reponse == bonne_reponse:
        print("Bonne réponse !")
        score += 1
    else:
        print(f"Mauvaise réponse... La réponse était : {bonne_reponse}")
    print("")
    print(f"Votre score est de {score}")

print("Bienvenue sur ce questionnaire ! ")
print("")
print("Répondez par a, b, c ou d")
print("")

score = 0

reponse = question_reponse(1,"France", "Paris", "Rome", "Ankara", "Lisbonne", "a")
reponse = question_reponse(2,"Madagscar", "Pekin", "Barcelone", "Antananarivo", "Obama", "c")
reponse = question_reponse(3,"Italie", "Tokyo", "Barcelone", "Londres", "Rome", "d")
reponse = question_reponse(4,"Japon", "Londres", "Tokyo", "Ankara", "Lisbonne", "b")