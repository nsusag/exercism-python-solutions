def spiral_matrix(size):
    output = [] 
    if size == 0:
        return output
    while len(output) < size:
        output.append([None for i in range(0, size)])
    x = 0 
    y = 0
    current = 1
    direction = 0
    while current <= size ** 2:
        if y == size or x == size or output[y][x] != None:
            if direction == 0:
                x -= 1
                y += 1
            elif direction == 1:
                y -= 1
                x -= 1
            elif direction == 2:
                x += 1
                y -= 1
            elif direction == 3: 
                y += 1
                x += 1
            direction = (direction + 1) % 4
        output[y][x] = current
        current += 1
        if direction == 0:
            x += 1
        elif direction == 1:
            y += 1
        elif direction == 2:
            x -= 1
        elif direction == 3:
            y -= 1
    print(output)
    return output
