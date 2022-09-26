def annotate(minefield):
    # Function body starts here
    if minefield == []:
        return []
    first_len = len(minefield[0])
    for row in minefield:
        if len(row) != first_len:
            raise ValueError("Invalid input")
    output = []
    for i, row in enumerate(minefield):
        newrow = []
        for j, char in enumerate(row): 
            if char == '*':
                newrow.append(char)
            elif char == ' ': 
                min_row = i - 1
                max_row = i + 2
                if i == 0:
                    min_row = i
                if i == len(minefield) - 1:
                    max_row = i + 1
                min_char = j - 1
                max_char = j + 2
                if j == 0:
                    min_char = j
                if j == len(row) - 1:
                    max_char = j + 1
                mine_count = 0 
                print(i, j)
                print(min_row, max_row, min_char, max_char)
                for row_count in range(min_row, max_row):
                    current_row = minefield[row_count]  
                    for char_count in range(min_char, max_char):
                        print(char_count)
                        if current_row[char_count] == '*':
                            mine_count += 1
                if mine_count == 0:
                    newrow.append(' ')
                else:
                    newrow.append(str(mine_count))  
            else:
                raise ValueError("Invalid input") 
        output.append("".join(newrow))
    print(output)
    return output
