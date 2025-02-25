# Les 3 fonctions : 

def demander_reponse_numerique_user(min, max):
    reponse_str = input(f"Votre réponse (entre {min} et {max}): ")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        else:
            print(f"ERREUR : Vous devez rentrer un nombre entier entre {min} et {max}")
    except:
        print("ERREUR : vous devez rentrer uniquement des chiffres")
    return demander_reponse_numerique_user(min, max)

def question_reponse(question):
    titre_question = question[0]
    choix = question[1]

    bonne_reponse = question[2]

    print(f"{titre_question}")

    for i in range(len(choix)):
        print(f" {i+1} - {choix[i]}")

    print()
    resultat_score = False

    reponse_int = demander_reponse_numerique_user(1, len(choix))

    if choix[reponse_int - 1].lower() == bonne_reponse.lower():
        print("Bonne réponse !")
        resultat_score = True
    else:
        print(f"Mauvaise réponse... La réponse était : {bonne_reponse}")
    print("")
    return resultat_score

def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if question_reponse(question):
            score += 1
    print(f"Votre score final est de {score} sur {len(questionnaire)}")

# Le code : 

print("Bienvenue sur ce questionnaire ! ")
print("")

questionnaire = (
    ("Quelle est la capitale de la France ?", ("Paris", "Rome", "Ankara", "Lisbonne", "Lille"), "Paris"), 
    ("Quelle est la capitale de Madagascar ?", ("Pekin", "Barcelone", "Antananarivo", "Obama"), "Antananarivo"), 
    ("Quelle est la capitale de l'Espagne' ?", ("Dublin", "Rome", "Madrid"), "Madrid")
    )

lancer_questionnaire(questionnaire)