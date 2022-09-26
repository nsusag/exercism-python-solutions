def is_armstrong_number(number):
    string = str(number)
    result = 0
    for char in string:
        result += (int(char) ** len(string))
    return result == number
