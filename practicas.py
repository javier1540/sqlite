def positionLetter(text):
    for n in range(len(text)):
        print(text[n])

def alphabet_position(text):
    capLetters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    lowLetters = "abcdefghijklmnñopqrstuvwxyz"
    positions = ""
    for positionLetter in range(len(text)):
        letter = text[positionLetter]
        capPosition = capLetters.find(letter)
        lowPosition = lowLetters.find(letter)
        alphaPosition = ""
        if capLetters.find(letter) != -1:
            positions = positions + str(capLetters.find(letter))
        elif lowLetters.find(letter) != -1:
            positions = positions + str(lowLetters.find(letter))
    return positions

print(alphabet_position("Javier"))


"""
Lo que hace este programa es devolver una cadena con la posicion de cada letra que se pone como parametro al invocar la funcion
alphabet_position() 
"""