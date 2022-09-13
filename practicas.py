def positionLetter(text):
    for n in range(len(text)):
        print(text[n])

def alphabet_position(text):
    capLetters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    lowLetters = "abcdefghijklmnñopqrstuvwxyz"
    positions = ""
    for positionLetter in range(len(text)):
        letter = text[positionLetter]
        if capLetters.find(letter) or lowLetters.find(letter) != -1:
            positions += letter+" "
    return positions

print(alphabet_position("abc"))