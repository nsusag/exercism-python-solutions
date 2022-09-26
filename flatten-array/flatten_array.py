def flatten_helper(iterable, output):
    for element in iterable:
        if element is None:
            continue
        elif type(element) == list:
            flatten_helper(element, output)
        else:
            output.append(element)
    return 

def flatten(iterable):
    output = [] 
    for element in iterable:
        if element is None:
            continue
        elif type(element) == list:
            flatten_helper(element, output)
        else:
            output.append(element) 
    return output
