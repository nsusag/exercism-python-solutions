import copy

def can_chain(dominoes):
    if dominoes == []:
        return []
    elif len(dominoes) == 1:
        if dominoes[0][0] == dominoes[0][1]:
            return dominoes
        else:
            return None
    chain = [dominoes[0]] 
    new = copy.deepcopy(dominoes[1:])
    choices = []
    while len(new) != 0:
        if len(choices) < len(chain):
            possibilities = []
            for domino in new:
                if domino[0] == chain[-1][1]:
                    possibilities.append(domino)
                elif domino[1] == chain[-1][1]:
                    possibilities.append((domino[1], domino[0]))
            choices.append(possibilities)
        if choices[-1] == []: 
            for element in choices[::-1]:
                if choices[-1] != []:
                    break
                new.append(chain[-1])
                del chain[-1]
                del choices[-1] 
            if choices == []:
                return None
        if choices[-1][0] in new:
            del new[new.index(choices[-1][0])]
        else:
            del new[new.index((choices[-1][0][1], choices[-1][0][0]))]
        chain.append(choices[-1][0])
        del choices[-1][0]
        if 0 == len(new) and chain[0][0] != chain[-1][1]:
            new.append(chain[-1])
            del chain[-1]
    return chain 
