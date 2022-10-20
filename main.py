
def getLines(filename):
    with open(filename, 'r') as file:
        result = file.read().rstrip()
    return result

def isSymmetric(word):
    if word[0] is not word[-1]:
        return False
    if not word and (word[0] is word[-1]):
        word.pop(0)
        if not word:
            word.pop(-1)
        return isSymmetric(word)
    return True

def f(line, symbols):
    line = line.lower()
    for symbol in symbols:

        line = line.replace(symbol, "")

    words = line.split()
    symmetricWords = []
    for word in words:
        if isSymmetric(word):
            symmetricWords.append(word)
    print("Symmetric words: " + str(symmetricWords))
    return line


if __name__ == '__main__':
    filename = 'text.txt'
    symbols = [".", ",", "-", "—", "(", ")"]

    line = getLines('text.txt')
    resultLine = f(line, symbols)
    print(resultLine)

