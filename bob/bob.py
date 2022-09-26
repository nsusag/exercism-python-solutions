def is_question(hey_bob): 
    index = 0
    for i, char in enumerate(hey_bob):
        if char == "?":
            index = i
    for i, char in enumerate(hey_bob):
        if i > index:
            if not char.isspace():
                return False
    return index > 0

def is_all_caps(hey_bob):
    num_of_letters = 0 
    for char in hey_bob:
        if char.isalpha():
            num_of_letters += 1
            if not char.isupper():
                return False
    return num_of_letters > 0

def is_all_spaces(hey_bob):
    for char in hey_bob:
        if not char.isspace():
            return False
    return True

def response(hey_bob):
    if is_question(hey_bob):
        if is_all_caps(hey_bob):
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    elif is_all_spaces(hey_bob):
        return "Fine. Be that way!"
    elif is_all_caps(hey_bob):
        return "Whoa, chill out!"
    else:
        return "Whatever." 

