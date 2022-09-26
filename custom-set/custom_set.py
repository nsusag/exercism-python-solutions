class CustomSet:
    def __init__(self, elements=[]):
        newset = []
        for element in elements:
            if element not in newset:
                newset.append(element)
        self.elements = newset

    def isempty(self):
        return self.elements == []

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        for element in self.elements:
            if element not in other:
                return False
        return True

    def isdisjoint(self, other):
        for element in self.elements: 
            if element in other:
                return False
        return True

    def __eq__(self, other):
        return sorted(self.elements) == sorted(other.elements) 

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def intersection(self, other):
        newlst = []
        for element in self.elements:
            if element in other.elements:
                newlst.append(element)
        return CustomSet(newlst)

    def __sub__(self, other):
        newlst = []
        for element in self.elements:
            if element not in other.elements:
                newlst.append(element)
        self.elements = newlst
        return self

    def __add__(self, other):
        for element in other.elements: 
            if element not in self.elements:
                self.elements.append(element)
        return self
