import random
import string
import syllabify


def random_word_generator():
    words_input = input("Введіть слова через кому: ")

    words = [
        word.strip().strip(string.punctuation)
        for word in words_input.split(",")
    ]

    words = [word for word in words if word]

    if not words:
        print("Ви не ввели жодного слова!")
        return

    all_syllables = []

    for word in words:
        syllables = syllabify.syllabify(word)
        all_syllables.extend(syllables)

    if len(all_syllables) < len(words):
        print("Недостатньо складів для генерації слова!")
        return

    random_syllables = random.sample(all_syllables, len(words))
    random_word = "".join(random_syllables)

    print("Згенероване слово:", random_word)


random_word_generator()