import random

class Cipher:
    def __init__(self, key=None):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if key == None:
            new_key = []
            for i in range(1, 101):
                new_key.append(random.choice(self.alphabet)) 
            self.key = "".join(new_key)
        else:
            self.key = key 

    def encode(self, text):
        output = []
        for i, char in enumerate(text):
            output.append(self.alphabet[(self.alphabet.index(char) + self.alphabet.index(self.key[i % len(self.key)])) % 26])
        return "".join(output)

    def decode(self, text):
        output = []
        for i, char in enumerate(text):
            output.append(self.alphabet[(self.alphabet.index(char) - self.alphabet.index(self.key[i % len(self.key)])) % 26])
        return "".join(output)
        
