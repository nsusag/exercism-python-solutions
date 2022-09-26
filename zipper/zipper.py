import copy

class Zipper:
    def __init__(self, tree, upward=[]):
        self.upward = upward
        self.tree = tree

    @staticmethod
    def from_tree(tree):
        return Zipper(tree, [])

    def value(self): 
        return self.tree["value"]

    def set_value(self, value):
        self.tree["value"] = value  
        return self

    def left(self):
        if self.tree != None and self.tree["left"] != None:
            self.upward.append(("left", "right", self.tree["value"], self.tree["right"]))
            self.tree = self.tree["left"]
            return self 
        return None

    def set_left(self, value):
        self.tree["left"] = value
        return self

    def right(self):
        if self.tree != None and self.tree["right"] != None:
            self.upward.append(("right", "left", self.tree["value"], self.tree["left"]))
            self.tree = self.tree["right"]
            return self 
        return None

    def set_right(self, value):
        self.tree["right"] = value
        return self

    def up(self):  
        if self.upward != []: 
            newtree = {}
            newtree["value"] = self.upward[-1][2]
            newtree[self.upward[-1][0]] = self.tree
            newtree[self.upward[-1][1]] = self.upward[-1][3]
            self.tree = newtree 
            del self.upward[-1]
            return self 
        return None

    def to_tree(self):
        while self.upward != []:
            self.up()
        return self.tree 
