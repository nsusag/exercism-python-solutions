def saddle_points(matrix):
    output = []
    for i in range(1, len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise ValueError("Matrix is irregular")
    for x, row in enumerate(matrix):
        for y, element in enumerate(row): 
            if element < max(row):
                continue 
            else:
                for i, thing in enumerate(matrix):
                    if thing[y] < element:
                        break
                    if i == (len(matrix) - 1):
                        output.append({"row" : x + 1, "column" : y + 1})
    print(output)
    return output

