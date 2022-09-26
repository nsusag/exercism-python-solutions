import random

class Robot:
    def __init__(self):
        self.uppers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]  
        name = []
        for i in range(0, 2):
            name.append(random.choice(self.uppers))
        for i in range(2, 5):
            name.append(str(random.randint(0, 9)))
        self.name = "".join(name)
    def reset(self):
        random.seed() 
        name = []
        for i in range(0, 2):
            name.append(random.choice(self.uppers))
        for i in range(2, 5):
            name.append(str(random.randint(0, 9)))
        self.name = "".join(name)
