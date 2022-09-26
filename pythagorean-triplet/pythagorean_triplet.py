import math

def triplets_with_sum(number):

    # First solution (very slow)
    '''
    output = [] 
    for i in range(number, 1, -1):   
        j = number - i
        k = 0
        if j > 2 * i:
            break 
        while j >= k:
            print(i, j, k)
            if j > i:
                k += j - i
                j -= j - i
            if (k ** 2) + (j ** 2) == i ** 2 and k > 0:
                output.append([k, j, i])
            k += 1
            j -= 1
    print(output)
    return output
    '''

    # Second solution (also very slow)
    '''
    output = []
    j = number // 2
    k = 1
    while j > number // 4:
        while k < j:
            i = math.sqrt((k ** 2) + (j ** 2)) 
            if i + j + k == number:
                output.append([int(i), j, k])
            k += 1
        j -= 1
        k = 1
    print(output)
    return output
    '''

    # Euclid's formula (much faster)
    output = [] 
    m = 2
    n = 1 
    k = 1
    while k <= number / 6:
        while k * m <= number / 6:
            if k * ((2 * m) * (m + n)) > number:
                break
            while n < m:
                print(m, n)
                a = k * ((m ** 2) - (n ** 2))
                b = 2 * k * m * n
                c = k * ((m ** 2) + (n ** 2))
                total = a + b + c
                if total == number and a != 0 and b != 0:  
                    if a < b and [a, b, c] not in output:
                        output.append([a, b, c])
                    elif b < a and [b, a, c] not in output:
                        output.append([b, a, c])
                elif total > number:
                    break 
                n += 1
            m += 1
            n = 1
        k += 1
        m = 2
        n = 1
    print(output)
    return output
    
def triplets_in_range(start, end):
    pass

def is_triplet(triplet):
    pass
