def translate(text):
    vowels = ["a", "e", "i", "o", "u"]
    output = []
    for word in text.split():
        lst = list(word)
        if len(lst) == 2 and lst[1] == 'y':
            lst.append(lst[0])
            del lst[0]  
            lst.append("a")
            lst.append("y")
        elif lst[0] in vowels or (lst[0:2] == ["x", "r"]) or (lst[0:2] == ["y", "t"]):   
            lst.append("a") 
            lst.append("y")
        else:
            i = 0
            while lst[0] not in vowels:
                if i > 1 and lst[0] == "y":
                    break
                elif lst[0] == "q" and lst[1] == "u":
                    lst.append(lst[0])
                    lst.append(lst[1])
                    del lst[0]
                    del lst[0] 
                    break
                lst.append(lst[0]) 
                del lst[0]
                i += 1
            lst.append("a") 
            lst.append("y") 
        output.append("".join(lst)) 
    return " ".join(output)
