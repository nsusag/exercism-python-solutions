def isnumber(word):
    for char in word:
        if not char.isdigit() and char != "-" and char != ".":
            return False
    return True

def answer(question):
    split = question[:len(question) - 1].split()
    buff = [] 
    operation = 0
    print(split)
    for i, word in enumerate(split):
        print(word)
        if isnumber(word):
            if buff == [] and operation == 0:
                buff.append(int(word))
            elif buff != [] and operation != 0:
                if operation == 1:
                    buff[0] += int(word)
                    operation = 0
                elif operation == 2:
                    buff[0] -= int(word)
                    operation = 0
                elif operation == 3:
                    buff[0] *= int(word)
                    operation = 0
                elif operation == 4:
                    buff[0] /= int(word)
                    operation = 0
            else:
                raise ValueError("Numbers are not separated by operation words.")
        elif word == "plus" and operation == 0:
            operation = 1
        elif word == "minus" and operation == 0:
            operation = 2
        elif word == "multiplied" and split[i + 1] == "by" and operation == 0:
            operation = 3
        elif word == "divided" and split[i + 1] == "by" and operation == 0:
            operation = 4
        elif word not in ["What", "is", "by"]:
            raise ValueError("Unexpected word found")
    if buff == [] or operation != 0:
        raise ValueError("No output")
    else:
        return buff[0]

