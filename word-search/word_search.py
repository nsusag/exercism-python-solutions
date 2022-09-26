class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle 

    def search(self, word): 
        print(word)
        for lineno, line in enumerate(self.puzzle):
            for charno, char in enumerate(line):
                print(lineno, charno, char)
                if word[0] == char: 
                    print("Char is first letter")
                    if len(line) - charno >= len(word):
                        # checks if written left to right
                        for i in range(1, len(word)):
                            if word[i] != line[charno + i]:
                                break
                            elif i == len(word) - 1:
                                return(Point(charno, lineno), Point(charno + i, lineno))
                        # checks if written diagonally from bottom left to top right 
                        if lineno >= len(word) - 1:
                            for i in range(1, len(word)):
                                if self.puzzle[lineno - i][charno + i] != word[i]:
                                    break
                                elif i == len(word) - 1:
                                    return(Point(charno, lineno), Point(charno + i, lineno - i))
                        # checks if written diagonally from top left to bottom right
                        if len(self.puzzle) - lineno >= len(word):
                            for i in range(1, len(word)):
                                if self.puzzle[lineno + i][charno + i] != word[i]:
                                    break
                                elif i == len(word) - 1:
                                    return(Point(charno, lineno), Point(charno + i, lineno + i))
                    if charno >= len(word) - 1:
                        # checks if written right to left
                        for i in range(1, len(word)):
                            if word[i] != line[charno - i]:
                                break
                            elif i == len(word) - 1:
                                return(Point(charno, lineno), Point(charno - i, lineno))
                        # checks if written diagonally from bottom right to top left 
                        if lineno >= len(word) - 1:
                            for i in range(1, len(word)):
                                if self.puzzle[lineno - i][charno - i] != word[i]:
                                    break
                                elif i == len(word) - 1:
                                    return(Point(charno, lineno), Point(charno - i, lineno - i))
                        # checks if written diagonally from top right to bottom left
                        if len(self.puzzle) - lineno >= len(word):
                            for i in range(1, len(word)):
                                if self.puzzle[lineno + i][charno - i] != word[i]:
                                    break
                                elif i == len(word) - 1:
                                    return(Point(charno, lineno), Point(charno - i, lineno + i))
                    # checks if written bottom to top
                    if lineno >= len(word) - 1: 
                        for i in range(1, len(word)):
                            if self.puzzle[lineno - i][charno] != word[i]:
                                break
                            elif i == len(word) - 1:
                                return(Point(charno, lineno), Point(charno, lineno - i))
                    # checks if written top to bottom
                    if len(self.puzzle) - lineno >= len(word) - 1: 
                        for i in range(1, len(word)):
                            if self.puzzle[lineno + i][charno] != word[i]:
                                break
                            elif i == len(word) - 1:
                                return(Point(charno, lineno), Point(charno, lineno + i))
        return
