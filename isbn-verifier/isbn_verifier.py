def is_valid(isbn): 
    digits = []
    for char in isbn:
        if char.isdigit():
            digits.append(int(char))
        elif char == 'X' and len(digits) == 9:
            digits.append(10)
    if len(digits) != 10:
        return False
    return (digits[0] * 10 + digits[1] * 9 + digits[2] * 8 + digits[3] * 7 + digits[4] * 6 + digits[5] * 5 + digits[6] * 4 + digits[7] * 3 + digits[8] * 2 + digits[9] * 1) % 11 == 0
