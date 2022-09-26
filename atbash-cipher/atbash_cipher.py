# from string import maketrans
import string

def encode(plain_text): 
    new_string = ""
    i = 0
    for char in plain_text: 
        if char.isalpha() or char.isdigit():
            new_string = new_string + char
            i += 1 
        if i == 5:
            new_string = new_string + " " 
            i = 0
    new_string = new_string.rstrip()
    return new_string.translate(new_string.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba"))

def decode(ciphered_text): 
    new_string = ""
    for char in ciphered_text:
        if char.isalpha() or char.isdigit():
            new_string = new_string + char
    return new_string.translate(new_string.maketrans("zyxwvutsrqponmlkjihgfedcba", "abcdefghijklmnopqrstuvwxyz"))
