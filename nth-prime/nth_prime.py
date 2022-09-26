def prime(number):
    if number < 1:
        raise ValueError("IDIOT.")
    elif number == 1:
        return 2
    else:
        primelist = [2]
        current = 1
        while len(primelist) != number:
            current += 2
            for i, prime in enumerate(primelist): 
                if current % prime == 0:
                    break
                if i == (len(primelist) - 1):
                    primelist.append(current) 
        print(current)
        return current
