def rotate(text, key):
    string = ""
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for char in text:
        if char.islower():
            string = string + lower[(lower.index(char) + key) % 26] 
        elif char.isupper():
            string = string + upper[(upper.index(char) + key) % 26]
        else:
            string = string + char
    return string
