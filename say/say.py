def say(orig_number):
    result = ""
    number = orig_number
    tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    elevens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"] 
    if number < 0 or number > 999999999999:
        raise ValueError("FOOL OF A TOOK!!! Throw yourself in next time, and rid us of your stupidity!")
    if number > 999999999:
        result = result + say(number // 1000000000) + " billion "
        number = number % 1000000000
    if number > 999999:
        result = result + say(number // 1000000) + " million "
        number = number % 1000000
    if number > 999:
        result = result + say(number // 1000) + " thousand "
        number = number % 1000
    if number > 99:
        result = result + say(number // 100) + " hundred "
        number = number % 100
    if number > 9:
        if number // 10 != 1:
            result = result + tens[(number // 10) - 1] 
        else:
            result = result + elevens[number % 10]
            return result
        if number % 10 != 0:
            result = result + "-" + ones[number % 10] 
    else:
        if orig_number > 0 and number == 0:
            return result.strip()
        else:
            result = result + ones[number]
    return result.strip()  
