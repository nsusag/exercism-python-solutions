def convert(input_grid):
    nums = [[" _ ", "| |", "|_|", "   "], ["   ", "  |", "  |", "   "], [" _ ", " _|", "|_ ", "   "], [" _ ", " _|", " _|", "   "], ["   ", "|_|", "  |", "   "], [" _ ", "|_ ", " _|", "   "], [" _ ", "|_ ", "|_|", "   "],  [" _ ", "  |", "  |", "   "], [" _ ", "|_|", "|_|", "   "], [" _ ", "|_|", " _|", "   "]] 
    if len(input_grid) % 4 != 0:
        raise ValueError("Grid is not correct length")
    for i, line in enumerate(input_grid):
        if i > 0 and len(line) != len(input_grid[i - 1]):
            raise ValueError("Lengths of lines are not equal")
        elif len(line) % 3 != 0:
            raise ValueError("Line lengths must be divisible by 3")
    current = 0
    currentline = 0
    output = []
    while current < len(input_grid[0]):
        num = []
        for i in range(currentline, currentline + 4): 
            num.append(input_grid[i][current:current + 3])
        for i in range(0, 10):
            if num == nums[i]:
                output.append(str(i))
                break
            elif i == 9:
                output.append("?")
        current += 3
        if current >= len(input_grid[0]) and len(input_grid) - currentline > 4:
            currentline += 4
            current = 0
            output.append(",")
    return "".join(output)

