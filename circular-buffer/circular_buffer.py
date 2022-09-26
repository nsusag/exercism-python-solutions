class BufferFullException(Exception):
    pass

class BufferEmptyException(Exception):  
    pass

class CircularBuffer:
    def __init__(self, capacity):
        self.list = []
        for i in range(0, capacity):
            self.list.append(None)
        self.oldest = 0

    def read(self):
        for i, element in enumerate(self.list):
            if element != None and i == self.oldest: 
                output = element
                self.list[i] = None
                self.oldest = (self.oldest + 1) % len(self.list)
                print(self.list, self.oldest)
                return output 
        print(self.list, self.oldest)
        raise BufferEmptyException("Buffer is empty") 

    def write(self, data):
        for i in range(self.oldest, self.oldest + len(self.list)):
            if self.list[i % len(self.list)] == None:
                self.list[i % len(self.list)] = data
                print(self.list, self.oldest)
                return
        print(self.list, self.oldest)
        raise BufferFullException("Buffer is full")

    def overwrite(self, data):
        for i in range(self.oldest, self.oldest + len(self.list) + 1):
            if self.list[i % len(self.list)] == None:
                self.list[i % len(self.list)] = data
                print(self.list, self.oldest)
                return
            elif i == self.oldest + len(self.list):
                self.list[i % len(self.list)] = data
                self.oldest = (self.oldest + 1) % len(self.list)
                print(self.list, self.oldest)

    def clear(self):
        for i in range(0, len(self.list)):
            self.list[i] = None
