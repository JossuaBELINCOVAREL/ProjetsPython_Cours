def question_reponse(question):
    titre_question = question[0]
    choix = question[1]
    global score

    bonne_reponse = question[2]

    print(f"{titre_question}")

    for choix in question[1]:
        print(f" - {choix}")

    print()

    reponse = input("Votre réponse : ")       

    if reponse.lower() == bonne_reponse.lower():
        print("Bonne réponse !")
        score =+1
        print(f"Votre score est de {score}")
    else:
        print(f"Mauvaise réponse... La réponse était : {bonne_reponse}")
        print(f"Votre score est de {score}")
    print("")

print("Bienvenue sur ce questionnaire ! ")
print("")

score = 0

question1 = ("Quelle est la capitale de la France ?", ("Paris", "Rome", "Ankara", "Lisbonne"), "Paris")
question2 = ("Quelle est la capitale de Madagascar ?", ("Pekin", "Barcelone", "Antananarivo", "Obama"), "Antananarivo")

question_reponse(question1)
question_reponse(question2)