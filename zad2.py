with open('plik.txt', 'r') as file:
    letterOccuerences = {}
    for letter in file.read():
        if letter in letterOccuerences:
            letterOccuerences[letter] = letterOccuerences[letter] + 1
        else:
            letterOccuerences[letter] = 1
    print(letterOccuerences)
