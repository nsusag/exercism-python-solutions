import copy

class StackUnderflowError(Exception):
    pass


def evaluate(input_data):
    stack = []
    userDefinedWords = {}
    for command in input_data:
        split = command.split()
        if split[0] == ":" and split[-1] == ";":
            if split[1].isdigit():
                raise ValueError("Cannot redefine numbers")
            newsplit = split 
            for word in split[2:-1]:
                if word in userDefinedWords:
                    newsplit = []
                    for i, thing in enumerate(split):
                        print(newsplit)
                        if thing in userDefinedWords and i > 1:
                            print(userDefinedWords[thing])
                            newsplit.extend(userDefinedWords[thing])
                        else:
                            newsplit.append(thing) 
            print(newsplit)
            userDefinedWords[newsplit[1].lower()] = newsplit[2:-1]
            print(userDefinedWords)
        else:
            newsplit = []
            for element in split: 
                if element.lower() in userDefinedWords:
                    for thing in userDefinedWords[element.lower()]:
                        newsplit.append(thing)
                else:
                    newsplit.append(element)
            print(userDefinedWords, newsplit)
            for element in newsplit:
                if element.isdigit():
                    stack.append(int(element))
                elif element in ["+", "-", "*", "/"]:
                    if len(stack) < 2:
                        raise StackUnderflowError("Insufficient arguments")
                    else:
                        if element == "+":
                            temp = stack[-2] + stack[-1]
                            del stack[-2:]
                            stack.append(temp)
                        elif element == "-":
                            temp = stack[-2] - stack[-1]
                            del stack[-2:]
                            stack.append(temp)
                        elif element == "*":
                            temp = stack[-2] * stack[-1]
                            del stack[-2:]
                            stack.append(temp)
                        elif element == "/":
                            temp = stack[-2] // stack[-1]
                            del stack[-2:]
                            stack.append(temp)
                elif element.lower() == "dup":
                    if stack == []:
                        raise StackUnderflowError("Insufficient arguments")
                    stack.append(stack[-1])
                elif element.lower() == "drop":
                    if stack == []:
                        raise StackUnderflowError("Insufficient arguments")
                    del stack[-1]
                elif element.lower() == "swap":
                    if len(stack) < 2: 
                        raise StackUnderflowError("Insufficient arguments")
                    temp = stack[-1]
                    print(temp)
                    del stack[-1]
                    print(temp)
                    stack.insert(-1, temp)
                elif element.lower() == "over":
                    if len(stack) < 2: 
                        raise StackUnderflowError("Insufficient arguments")
                    stack.append(stack[-2])       
                else:
                    raise ValueError("Unrecognized word")
                print(element, stack)
    return stack
