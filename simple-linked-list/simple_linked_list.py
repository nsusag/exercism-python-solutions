class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

    def value(self):
        return self.value 

    def __next__(self):
        return self.next
    
class LinkedList(object): 
    def __init__(self, values=[]):
        

    def __len__(self):
        counter = 0
        for element in self:
            counter += 1
        return counter 

    def __iter__(self):
        

    def head(self):
        if self.__len__() == 0:
            raise EmptyListException
        return self.value 

    def push(self, value):
        self = Node(value, self)
        return

    def pop(self):
        if self.__len__() == 0:
            raise EmptyListException
        output = self.value 
        self = self.next()
        return output

    def reversed(self):
        pass 
        
class EmptyListException(Exception):
    pass
