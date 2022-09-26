def istriangle(sides):
    return len(sides) == 3 and (sides[0] + sides[1] >= sides[2]) and (sides[0] + sides[2] >= sides[1]) and (sides[1] + sides[2] >= sides[0])

def equilateral(sides): 
    return sides[0] == sides[1] and sides[0] == sides[2] and sides[0] > 0

def isosceles(sides):
    return istriangle(sides) and (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]) 

def scalene(sides):
    return istriangle(sides) and sides[0] != sides[1] != sides[2] != sides[0]
