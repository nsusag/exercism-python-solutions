import copy
from json import dumps

class Tree:
    def __init__(self, label, children=[]):
        self.label = label
        self.children = children

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node): 
        # Deals with the edge case in which no changes need be done
        if from_node == self.label:
            return self
        parents = []
        # This while loop finds the location of from_node in the tree, and saves every node on the path to from_node, as well as all their children
        while self.label != from_node:
            # If there is a child of the current to check for from_node, check it
            if self.children != []:
                parents.append([self.label, self.children, 0])
                self = self.children[0]
            # If there are no children, go back to the most recently checked node which still has unchecked children
            else:
                while parents != [] and parents[-1][2] + 1 == len(parents[-1][1]): 
                    del parents[-1]
                if parents == []:
                    raise ValueError("No such node exists.")
                parents[-1][2] += 1
                self = parents[-1][1][parents[-1][2]]
            print("self:", self, "parents:", parents)
        # Gets rid of the children which are part of the path to from_node
        for parent in parents:
            del parent[1][parent[2]]
        # Converts all of the elements of parents into a tree
        for i in range(1, len(parents)):
            parents[i][1].append(Tree(parents[i - 1][0], parents[i - 1][1])) 
        newlst = copy.copy(self.children) 
        newlst.append(Tree(parents[-1][0], parents[-1][1]))
        self.children = newlst
        # Makes this tree a child of from_node
        return self 

    def path_to(self, from_node, to_node):
        # Centers the tree on from_node
        self = self.from_pov(from_node)
        parents = []
        tree = self
        # Employs the same node-finding while loop as in from_pov
        while tree.label != to_node: 
            if tree.children != []:
                parents.append([tree.label, tree.children, 0])
                tree = tree.children[0]
            else:
                while parents != [] and parents[-1][2] + 1 == len(parents[-1][1]): 
                    del parents[-1]
                if parents == []:
                    raise ValueError("No such node exists.")
                parents[-1][2] += 1
                tree = parents[-1][1][parents[-1][2]]
        output = []
        for parent in parents:
            output.append(parent[0])
        output.append(to_node)
        return output
