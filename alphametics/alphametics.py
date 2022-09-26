import random 

def factorial(num):
    output = 1
    while num > 1:
        output *= num
        num -= 1
    return output

def pickn(n, lst):
    output = []
    numofcombos = factorial(len(lst)) // (factorial(n) * factorial(len(lst) - n))
    while len(output) != numofcombos:
        current = []
        while len(current) != n: 
            char = random.choice(lst) 
            if char not in current:
                current.append(char)
        current.sort()
        if current not in output:
            output.append(current)
    return output
    
def permutations(lst):
    output = [] 
    for i in range(0, len(lst)): 
        if len(lst) == 1:
            return [lst]
        cpylst = lst[:i] + lst[i + 1:]
        for perm in permutations(cpylst):
            perm.append(lst[i])
            output.append(perm) 
    return output

def solve(puzzle): 
    letters = [] 
    for i, char in enumerate(puzzle):
        if char.isalpha() and char not in letters:
            letters.append(char)
    perms = []
    combos = pickn(len(letters), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
    for combo in combos:
        current = permutations(combo)
        for perm in current:
            perms.append(perm) 
    for perm in perms:
        for i, element in enumerate(perm):
            perm[i] = str(element)
        transtable = str.maketrans("".join(letters), "".join(perm))
        newpuzzle = puzzle.translate(transtable)
        split = newpuzzle.split()
        for i, word in enumerate(split):
            if word == "+" or word == "=" or word == "==":
                del split[i] 
        for i, word in enumerate(split):
            if word[0] == "0":
                i -= 1
                break 
        if i < len(split) - 1:
            continue 
        split = list(map(int, split))
        if sum(split[:-1]) == split[-1]:
            outputdict = {}
            for i in range(0, len(letters)):
                outputdict[letters[i]] = int(perm[i])
            print(outputdict)
            return outputdict
    return None
