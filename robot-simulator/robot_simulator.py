# Globals for the directions
# Change the values as you see fit
EAST = 1 
NORTH = 0 
WEST = 3 
SOUTH = 2 

class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction 
        self.x = x
        self.y = y

    def move(self, string):
        for char in string:
            if char == "R":
                self.direction = (self.direction + 1) % 4
            elif char == "L":
                self.direction = (self.direction - 1) % 4
            elif char == "A":
                if self.direction == 0:
                    self.y += 1
                elif self.direction == 1:
                    self.x += 1
                elif self.direction == 2:
                    self.y -= 1
                elif self.direction == 3:
                    self.x -= 1

    @property
    def coordinates(self):
        return (self.x, self.y)

