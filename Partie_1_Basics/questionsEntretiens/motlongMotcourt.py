# Déterminer le mot le plus long / le mot le plus court dans une phrase

def get_min_max_words(s: str):
    s_split = s.split(" ")

    min_word = min(s_split, key=len)
    max_word = max(s_split, key=len)

    return (min_word, max_word)

phrase = "Plusieurs chasseuses sachant chasser savent chasser sans leurs chiens"

min_word, max_word = get_min_max_words(phrase)

print(f"Le mot le plus petit est : {min_word}")
print(f"Le mot le plus grand est : {max_word}")

