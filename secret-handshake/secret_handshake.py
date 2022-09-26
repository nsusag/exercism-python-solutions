def commands(number):
    output = []
    reverse = False
    if number >= 16:
        reverse = True
        number -= 16
    if number >= 8:
        output.append("jump")
        number -= 8 
    if number >= 4:
        output.append("close your eyes")
        number -= 4 
    if number >= 2:
        output.append("double blink")
        number -= 2
    if number >= 1: 
        output.append("wink")
        number -= 1
    if reverse: 
        return output
    return output[::-1]

commands(15)
