def encode(message, rails):
    output = []
    current = 0
    currentrail = 1
    distfrombottom = 2 * (rails - currentrail) 
    distfromtop = distfrombottom
    while currentrail <= rails:
        i = 0
        while current < len(message):
            output.append(message[current])
            if i % 2 == 0:
                current += distfrombottom 
            else:
                current += distfromtop
            i += 1
        current = currentrail
        currentrail += 1
        distfromtop = 2 * (currentrail - 1)
        if currentrail != rails:
            distfrombottom = 2 * (rails - currentrail)
        else:
            distfrombottom = distfromtop
    print("".join(output), len(output))
    return "".join(output)  

def decode(encoded_message, rails):
    print(encoded_message)
    output = [encoded_message[0]]
    currentrail = 1
    raillengths = []
    while currentrail <= rails:
        if currentrail == 1:            
            distfrombottom = 2 * (rails - currentrail) 
            distfromtop = distfrombottom
        elif currentrail == rails:
            distfromtop = 2 * (currentrail - 1)
            distfrombottom = distfromtop
        else:
            distfrombottom = 2 * (rails - currentrail) 
            distfromtop = 2 * (currentrail - 1)
        pos = currentrail - 1
        num_on_rail = 0
        i = 0
        while pos < len(encoded_message):
            num_on_rail += 1
            i += 1
            if (i % 2) == 0:
                pos += distfrombottom
            else:
                pos += distfromtop
        raillengths.append(num_on_rail)
        currentrail += 1
    print(raillengths)
    currentrail = 2
    numoncenter = 0
    numonends = 0
    goingdown = True
    while len(output) != len(encoded_message):     
        if currentrail == 1:
            goingdown = True
            numonends += 1
            numoncenter += 1
        elif currentrail == rails:
            goingdown = False
            numoncenter += 1
        if currentrail != 1 and currentrail != rails:
            output.append(encoded_message[sum(raillengths[0:currentrail - 1]) + numoncenter])
        elif currentrail == rails and rails > 4:
            output.append(encoded_message[sum(raillengths[0:currentrail - 1]) + numonends + 1])
        else:
            output.append(encoded_message[sum(raillengths[0:currentrail - 1]) + numonends])
        print("".join(output), currentrail)
        if goingdown:
            currentrail += 1
        else:
            currentrail -= 1 
    print("".join(output))
    return "".join(output)
