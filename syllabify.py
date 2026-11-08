def syllabify(word):
    vowels = "аоуеіиюєяїАОУЕІИЇЮЄЯ"
    
    syllables = []
    current_syllable = ""

    for char in word:
        current_syllable += char
        if char.lower() in vowels:
            syllables.append(current_syllable)
            current_syllable = ""

    if current_syllable:
        syllables.append(current_syllable)

    return syllables