alphabet = "abcdefghijklmnopqrstuvwxyz"

def encode(plain_text, a, b):
    # Checks a is coprime to m (length of alphabet, 26 in this case)
    for i in range(2, (a // 2) + 1):
        if a % i == 0 and 26 % i == 0:
            raise ValueError("a must be coprime to m.")
    # Cleaning the string by:
    # getting rid of all nonalphabetic characters 
    # converting all alphabetic characters to lowercase
    cleaned = [] 
    for char in plain_text: 
        if char.isalpha():
            cleaned.append(char.lower())
        elif char.isdigit():
            cleaned.append(char)
    # implements encryption function
    # and adds a space every 5 letters
    string = "".join(cleaned)
    output = []
    for i, char in enumerate(string):
        if char.isalpha():
            output.append(alphabet[(a * alphabet.index(char) + b) % 26])
        else:
            output.append(char)
        if (i + 1) % 5 == 0 and i != len(string) - 1: 
            output.append(' ')
    return "".join(output)
 
def decode(ciphered_text, a, b):
    # Checks a is coprime to m (length of alphabet, 26 in this case)
    for i in range(2, (a // 2) + 1):
        if a % i == 0 and 26 % i == 0:
            raise ValueError("a must be coprime to m.")
    # find modular multiplicative inverse
    i = 1
    while a * i % 26 != 1 and i < 26:
        i += 1
    # Decrypt
    output = []
    for char in ciphered_text:
        print(char)
        if char.isalpha():
            output.append(alphabet[(i * (alphabet.index(char) - b)) % 26])
        elif not char.isspace():
            output.append(char)
    return "".join(output)
