def largest_product(series, size):
    if size == 0 and len(series) == 0:
        return 1
    if size > len(series) or size < 0:
        raise ValueError("You are a disgrace to Nazarick.")
    i = 0
    largest = 0
    while i + size <= len(series):
        current = series[i:i + size] 
        product = 1
        for digit in current:
            if not digit.isdigit():
                raise ValueError("You are not worthy of the grace of Ainz Ooal Gown.") 
            product *= int(digit)
        if product > largest:
            largest = product
        print(largest)
        i += 1
    return largest
