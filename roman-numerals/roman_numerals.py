def roman_helper(number, magnitude):
    global chars
    if magnitude == 1:
        chars = ["I", "V", "X"]
    elif magnitude == 10:
        chars = ["X", "L", "C"]
    elif magnitude == 100: 
        chars = ["C", "D", "M"]
    else:
        chars = ["M"]
    result = ""
    if (number // magnitude) <= 3:
        for i in range(1, (number // magnitude) + 1):
            result = result + chars[0]
    elif (number // magnitude) == 4:
        result = result + chars[0] + chars[1]
    elif (number // magnitude) <= 8:
        result = result + chars[1]
        for i in range(1, (number // magnitude) - 4):
            result = result + chars[0] 
    else:
        result = result + chars[0] + chars[2]
    return result

def roman(number):
    if number < 1 or number > 3000:
        raise ValueError("Your numbers OBVIOUSLY aren't historically accurate, plebeian.")
    output = ""
    mag = 1000
    while mag != 0: 
        if number // mag > 0:
            output = output + roman_helper(number, mag)
            number %= mag
        mag //= 10
    return output
