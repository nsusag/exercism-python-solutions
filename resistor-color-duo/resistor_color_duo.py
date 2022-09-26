def value(colors):
    mag = 10 ** (len(colors) - 1) 
    if mag > 10:
        mag = 10
    output = 0 
    arr = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    for color in colors[:2]:
        output += mag * arr.index(color)
        mag = mag // 10
    return output
