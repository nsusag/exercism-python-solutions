class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        width = 1
        for char in self.matrix_string:
            if char == ' ':
                width += 1 
            elif char == '\n':
                break
        numbers = self.matrix_string.split()
        result = numbers[((index - 1) * width):(index * width)]
        for i in range(width):
            result[i] = int(result[i])
        return result

    def column(self, index):
       width = 1
       for char in self.matrix_string:
            if char == ' ':
                width += 1 
            elif char == '\n':
                break
       numbers = self.matrix_string.split()
       result = numbers[(index - 1)::width]
       for i in range(len(result)):
            result[i] = int(result[i])
       return result

