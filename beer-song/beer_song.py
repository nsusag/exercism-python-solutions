def recite(start, take=1):
    output = []  
    while take > 0:
        if start > 1:
            output.append("".join([str(start), " bottles of beer on the wall, ", str(start), " bottles of beer."]))
            start -= 1
            if start > 1:
                output.append("".join(["Take one down and pass it around, ", str(start), " bottles of beer on the wall."]))
            else:
                output.append("".join(["Take one down and pass it around, ", str(start), " bottle of beer on the wall."]))
        elif start == 1:
            output.append("".join([str(start), " bottle of beer on the wall, ", str(start), " bottle of beer."]))
            start -= 1
            output.append("Take it down and pass it around, no more bottles of beer on the wall.")
        elif start == 0:
            output.append("No more bottles of beer on the wall, no more bottles of beer.")
            start += 99
            output.append("".join(["Go to the store and buy some more, ", str(start), " bottles of beer on the wall."]))
        else:
            raise ValueError("Start is negative.")
        take -= 1
        if take > 0:
            output.append('')
    print(output)
    return output
