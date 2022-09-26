def decode(string):
    count = "" 
    output = ""
    for char in string:
        if char.isdigit():
            count = count + char
        elif count != "":
            i = 1
            while i < (int(count) + 1):
                output = output + char
                i += 1
            count = ""
        else:
            output = output + char
    return output

def encode(string):
    current_char = [] 
    output = ""
    for char in string:
        if current_char != [] and char != current_char[0]:
            count = ""
            if len(current_char) > 1:
                count = str(len(current_char))
            output = output + count + current_char[0] 
            current_char = []
        if current_char == [] or char == current_char[0]:
            current_char.append(char)
    if len(string) > 0:
        count = ""
        if len(current_char) > 1:
            count = str(len(current_char))
        output = output + count + current_char[0] 
    return output
