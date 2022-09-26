def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1

def concat(lists):
    if lists == []:
        return []
    elif length(lists) == 1:
        return lists[0]
    else:
        for lst in lists[1:]:
            lists[0] = lists[0] + lst
        return lists[0]

def filter(function, lst):
    output = []
    for element in lst:
        if function(element):
            output.append(element)
    return output

def length(lst):
    counter = 0
    for element in lst:
        counter += 1
    return counter

def map(function, lst):
    output = []
    for element in lst:
        output.append(function(element))
    return output
 
def foldl(function, lst, initial):
    for element in lst:
       initial = function(initial, element) 
    return initial

def foldr(function, lst, initial):
    for element in reverse(lst):
        initial = function(element, initial)
    return initial

def reverse(lst):
    counter = length(lst) - 1
    output = []
    while counter >= 0: 
        output.append(lst[counter])    
        counter -= 1
    return output
