def rebase(input_base, digits, output_base):
    if input_base < 2 or output_base < 2:
        raise ValueError("Please provide a valid base.")
    mag = input_base ** (len(digits) - 1) 
    num = 0
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("A digit is negative, or greater than the base")
        num += digit * mag
        mag = mag // input_base 
    output = []
    mag = 1
    while output_base * mag < num: 
        mag *= output_base
    while mag > 0: 
        output.append(num // mag)
        num -= (num // mag) * mag
        mag = mag // output_base
    return output 
