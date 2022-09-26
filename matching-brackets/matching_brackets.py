def is_paired(input_string): 
    opens = []
    for char in input_string:
        if char == '(' or char == '[' or char == '{':
            opens.append(char)
        elif char == ')' or char == ']' or char == '}':
            if opens == []:
                return False
            else:
                last = opens.pop()
                if (last == '(' and char != ')') or (last == '[' and char != ']') or (last == '{' and char != '}'):
                    return False
    return opens == []
