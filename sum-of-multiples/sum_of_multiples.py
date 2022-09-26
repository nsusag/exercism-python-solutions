def sum_of_multiples(limit, multiples):
    mults = set()
    for element in multiples:
        if element < limit and element > 0:
            p = element
            while p < limit:
                mults.add(p)
                p += element
    if mults != set():
        return sum(mults)
    else:
        return 0
