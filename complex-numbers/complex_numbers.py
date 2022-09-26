import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        if self.real == other.real and self.imaginary == other.imaginary:
            return True
        return False

    def __add__(self, other):
        self.real += other.real 
        self.imaginary += other.imaginary  
        print(self.real, self.imaginary)
        return self

    def __mul__(self, other):
        print(self.real, self.imaginary, other.real, other.imaginary)
        temp = self.real
        self.real = (self.real * other.real) - (self.imaginary * other.imaginary) 
        self.imaginary = (self.imaginary * other.real) + (temp * other.imaginary) 
        print(self.real, self.imaginary)
        return self

    def __sub__(self, other):
        self.real -= other.real 
        self.imaginary -= other.imaginary
        print(self.real, self.imaginary)
        return self

    def __truediv__(self, other):
        temp = self.real
        self.real = ((self.real * other.real) + (self.imaginary * other.imaginary)) / (other.real ** 2 + other.imaginary ** 2) 
        self.imaginary = ((self.imaginary * other.real) - (temp * other.imaginary)) / (other.real ** 2 + other.imaginary ** 2)
        print(self.real, self.imaginary)
        return self

    def __abs__(self):
        return math.sqrt(self.imaginary ** 2 + self.real ** 2)

    def conjugate(self):
        self.imaginary *= -1 
        print(self.real, self.imaginary)
        return self

    def exp(self):
        return ComplexNumber(math.e ** self.real, 0) * ComplexNumber(math.cos(self.imaginary), math.sin(self.imaginary))
