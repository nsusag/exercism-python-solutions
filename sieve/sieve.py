import time

start_time = time.time()

def primes(limit):
    primes = [i for i in range(2, limit + 1)] 
    p = 2
    i = 0
    while p < limit / 2:
        multiple = 2 * p
        while multiple <= limit:
            if multiple in primes:
                del primes[primes.index(multiple)]
            multiple += p
        i += 1
        p = primes[i]
    print(primes)
    return list(primes) 
    
primes(3571)
print("--- %s seconds ---" % (time.time() - start_time))
