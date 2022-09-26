def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("YOU DUN FUCKED UP.")
    largest = None
    factors = []
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1): 
            product = i * j       
            if (largest == None or product > largest) and ispalindrome(product):
                factors = []
                largest = product 
                factors.append([i, j])
            elif largest == product and ispalindrome(product):
                factors.append([i, j])
    print(largest, factors)
    return largest, factors
             
def ispalindrome(number):
    strnumber = str(number)
    for i in range(0, len(strnumber) // 2):
        if strnumber[i] != strnumber[len(strnumber) - 1 - i]:
            return False
    return True

def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("NO.")
    smallest = None
    factors = []
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1): 
            product = i * j       
            print(product)
            if (smallest == None or product < smallest) and ispalindrome(product):
                factors = []
                smallest = product 
                factors.append([i, j])
            elif smallest == product and ispalindrome(product):
                factors.append([i, j])
            elif smallest != None and product > smallest:
                break
    print(smallest, factors)
    return smallest, factors

