def square(number):
    if number < 1 or number > 64:
        raise ValueError("DUMMY.")
    result = 1
    for i in range(1, number):
        result *= 2
    return result

def total():
    total = 0 
    for i in range(1, 65):
        total += square(i) 
    return total 
