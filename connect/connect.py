class ConnectGame:
    def __init__(self, board):
        newboard = [] 
        for i in range(0, len(board)):
            if i == 0:
                current = []
            if board[i] == '\n':
                newboard.append(current)
                current = []
            elif not board[i].isspace(): 
                current.append(board[i])
        newboard.append(current)
        self.board = newboard

    def adjacent(self, point, lst, already):
        output = []
        if (point[0] - 1, point[1]) in lst and (point[0] - 1, point[1]) not in already:
            output.append((point[0] - 1, point[1]))
        if (point[0] + 1, point[1]) in lst and (point[0] + 1, point[1]) not in already: 
            output.append((point[0] + 1, point[1]))
        if (point[0], point[1] - 1) in lst and (point[0], point[1] - 1) not in already:
            output.append((point[0], point[1] - 1))
        if (point[0] + 1, point[1] - 1) in lst and (point[0] + 1, point[1] - 1) not in already:
            output.append((point[0] + 1, point[1] - 1))
        if (point[0] - 1, point[1] + 1) in lst and (point[0] - 1, point[1] + 1) not in already:
            output.append((point[0] - 1, point[1] + 1))
        if (point[0], point[1] + 1) in lst and (point[0], point[1] + 1) not in already:
            output.append((point[0], point[1] + 1))
        return output

    def get_winner(self):  
        Xcoords = []
        Ocoords = []
        for y in range(0, len(self.board)):
            for x in range(0, len(self.board[0])):
                if self.board[y][x] == 'X':
                    Xcoords.append((x, y))
                elif self.board[y][x] == 'O':
                    Ocoords.append((x, y))
        for point in Xcoords:
            if point[0] == 0:
                path = [point] 
                while path[-1][0] != len(self.board[0]) - 1: 
                    current = path[-1] 
                    adjacent = self.adjacent(current, Xcoords, path) 
                    if adjacent != []:
                        path.append(adjacent[0])
                    elif current != path[0]:
                        Xcoords.remove(current)
                        path = [point] 
                    else: 
                        break
                if path[-1][0] == len(self.board[0]) - 1:
                    return 'X'
        for point in Ocoords:
            if point[1] == 0:
                path = [point] 
                while path[-1][1] != len(self.board) - 1: 
                    current = path[-1] 
                    adjacent = self.adjacent(current, Ocoords, path) 
                    if adjacent != []:
                        path.append(adjacent[0])
                    elif current != path[0]:
                        Ocoords.remove(current)
                        path = [point] 
                    else: 
                        break
                if path[-1][1] == len(self.board) - 1:
                    return 'O'
        return ''
