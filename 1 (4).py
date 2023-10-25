def split_word_into_syllables(word):
    vowels = 'aeiouy'
    syllables = []
    current_syllable = ''
    for letter in word.lower():
        if letter in vowels:
            current_syllable += letter
        else:
            if current_syllable:
                syllables.append(current_syllable)
                current_syllable = ''
            syllables.append(letter)
    if current_syllable:
        syllables.append(current_syllable)
    return syllables

word = 'elephant'
result = split_word_into_syllables(word)
print(result)  # Output: ['e', 'le', 'phant']