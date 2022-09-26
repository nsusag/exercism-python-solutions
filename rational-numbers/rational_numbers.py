from __future__ import division

class Rational:
    def __init__(self, numer, denom):
        self.numer = numer 
        self.denom = denom 
        self.simplify()
        print(self) 

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        self.numer = self.numer * other.denom + other.numer * self.denom 
        self.denom = self.denom * other.denom
        print(self) 
        self.simplify()
        print(self) 
        return self

    def __sub__(self, other):
        self.numer = self.numer * other.denom - other.numer * self.denom 
        self.denom = self.denom * other.denom
        print(self)
        self.simplify()
        print(self)
        return self

    def __mul__(self, other):
        self.numer = self.numer * other.numer
        self.denom = self.denom * other.denom
        print(self)
        self.simplify()
        print(self)
        return self

    def __truediv__(self, other):
        if self.denom * other.numer != 0:
            self.numer = self.numer * other.denom 
            self.denom = other.numer * self.denom
            print(self)
            self.simplify()
            print(self)
        return self

    def __abs__(self):
        if self.numer < 0:
            self.numer *= -1
        if self.denom < 0:
            self.denom *= -1
        print(self)
        return self

    def __pow__(self, power):
        if power >= 0:
            self.numer = self.numer ** power 
            self.denom = self.denom ** power
        else:
            self.numer = self.denom ** abs(power)
            self.denom = self.numer ** abs(power)
        print(self)
        self.simplify()
        print(self)
        return self

    def __rpow__(self, base): 
        return ((base ** self.numer) ** (1 / self.denom)) 
    
    def simplify(self):
        if self.numer == 0:
            self.denom = 1
            return self
        if self.denom < 0:
            self.numer *= -1
            self.denom *= -1
        gcm = 1
        for multiple in range(min(abs(self.numer), abs(self.denom)), 1, -1): 
            print("multiple =", multiple)
            if self.numer % multiple == 0 and self.denom % multiple == 0:
                gcm = multiple
                break
        print("gcm =", gcm)
        self.numer = self.numer // gcm 
        self.denom = self.denom // gcm 
        return self
