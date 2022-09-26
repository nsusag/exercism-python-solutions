def factors(value):
    output = [] 
    if value < 2:
        return output
    for i in range(2, (value // 2) + 1):
        if value % i == 0:
            output.append(i)
            output.append(value // i)
            break
    for factor in output:
        newfactors = factors(factor)
        if newfactors != [factor]:
            del output[output.index(factor)]
            for element in newfactors:
                output.append(element)
    if output == []:
        output.append(value) 
    return output
