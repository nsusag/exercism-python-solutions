BLACK = "B"
WHITE = "W"
BLANK = " "
NONE = ""

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        Bstones = set() 
        Wstones = set() 
        blanks = set() 
        for y, line in enumerate(board):
            for x, char in enumerate(line):
                if char == "B":
                    Bstones.add((x, y))
                elif char == "W":
                    Wstones.add((x, y))
                else:
                    blanks.add((x, y))
        self.bstones = Bstones
        self.wstones = Wstones
        self.blanks = blanks
        self.board = board

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if x < 0 or x >= len(self.board[0]):
            raise ValueError("x is too low")
        if y < 0 or y >= len(self.board):
            raise ValueError("y is too low")
        if (x, y) not in self.blanks:
            return (NONE, set())
        coords = set([(x, y)]) 
        current = [(x, y)]
        new = []
        print(coords)
        while current != []:
            for element in current:
                print(coords, element, new)
                if (element[0] + 1, element[1]) in self.blanks:
                    if (element[0] + 1, element[1]) not in coords:
                        new.append((element[0] + 1, element[1]))
                    coords.add((element[0] + 1, element[1]))
                print(coords, element, new)
                if (element[0] - 1, element[1]) in self.blanks:
                    if (element[0] - 1, element[1]) not in coords:
                        new.append((element[0] - 1, element[1]))
                    coords.add((element[0] - 1, element[1]))
                print(coords, element, new)
                if (element[0], element[1] + 1) in self.blanks:
                    if (element[0], element[1] + 1) not in coords:
                        new.append((element[0], element[1] + 1))
                    coords.add((element[0], element[1] + 1))
                print(coords, element, new)
                if (element[0], element[1] - 1) in self.blanks:
                    if (element[0], element[1] - 1) not in coords:
                        new.append((element[0], element[1] - 1))
                    coords.add((element[0], element[1] - 1))
                print(coords, element, new)
            print(coords, current, new) 
            current = new 
            new = []
            print(current, new)
        owner = None
        for element in coords: 
            if (element[0] + 1, element[1]) in self.bstones or (element[0] - 1, element[1]) in self.bstones or (element[0], element[1] + 1) in self.bstones or (element[0], element[1] - 1) in self.bstones:
                if owner == None:
                    owner = BLACK
                elif owner == WHITE:
                    owner = NONE
            elif (element[0] + 1, element[1]) in self.wstones or (element[0] - 1, element[1]) in self.wstones or (element[0], element[1] + 1) in self.wstones or (element[0], element[1] - 1) in self.wstones:
                if owner == None:
                    owner = WHITE
                elif owner == BLACK:
                    owner = NONE
        if owner == None:
            owner = NONE
        return (owner, coords)

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        output = {BLACK : set(), WHITE : set(), NONE : set()}
        for element in self.blanks:
            owner, territory = self.territory(element[0], element[1])
            for space in territory:
                output[owner].add(space)
        return output
