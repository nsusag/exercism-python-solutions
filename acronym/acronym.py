def abbreviate(words):
    result = ""
    for i, char in enumerate(words):
        if char.isalpha() and (i == 0 or (not words[i - 1].isalpha() and words[i - 1] != "'")): 
            result = result + char.upper()
    return result
