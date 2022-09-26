def rows(letter):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] 
    output = []
    currentletter = 0 
    while currentletter >= 0:
        currentline = []
        for i in range(0, alphabet.index(letter) - currentletter):
            currentline.append(" ")
        currentline.append(alphabet[currentletter])
        for i in range(0, (2 * currentletter) - 1):
            currentline.append(" ")
        if currentletter > 0:
            currentline.append(alphabet[currentletter])
        for i in range(0, alphabet.index(letter) - currentletter):
            currentline.append(" ")
        if len(output) >= alphabet.index(letter): 
            currentletter -= 1
        else:
            currentletter += 1
        output.append("".join(currentline)) 
    print(output)
    return output
