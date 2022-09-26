def is_pangram(sentence):
    alphabet = ["a", "b", "c", "d", 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    chars = []
    for char in sentence:
        if char.isalpha():
            if char.lower() not in chars:
                chars.append(char.lower())
    for char in alphabet:
        if char not in chars:
            return False
    return True
