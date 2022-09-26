def transpose(lines):
    split = lines.split('\n') 
    lengths = []
    longest = 0
    for line in split:
        length = len(line)
        if length > longest: 
            longest = length
        lengths.append(length)
    currentx = 0
    currenty = 0
    output = []
    while currentx < longest:
        currentline = []
        while currenty < len(split):
            if currentx < len(split[currenty]):
                currentline.append(split[currenty][currentx])
            elif currentx < max(lengths[currenty:]):
                currentline.append(" ")
            currenty += 1
        if currentline != []:
            output.append("".join(currentline))
        currentx += 1
        currenty = 0
    return "\n".join(output)
