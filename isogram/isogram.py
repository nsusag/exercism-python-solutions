def is_isogram(string):   
    charlist = []
    charset = set()
    for char in string:
        if char.isalpha():
            charlist.append(char.lower())
            charset.add(char.lower())
    return len(charlist) == len(charset)
