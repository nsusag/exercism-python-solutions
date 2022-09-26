class Clock:
    def __init__(self, hour, minute):
        self.hour = (hour + (minute // 60)) % 24
        self.minute = minute % 60

    def __repr__(self):
        return str(self.hour).rjust(2, "0") + ":" + str(self.minute).rjust(2, "0")

    def __eq__(self, other):
        return ((self.hour + (self.minute // 60)) % 24) == ((other.hour + (other.minute // 60)) % 24) and self.minute % 60 == other.minute % 60 

    def __add__(self, minutes):
        self.hour = (self.hour + ((self.minute + minutes) // 60)) % 24
        self.minute = (self.minute + minutes) % 60
        return self.__repr__()

    def __sub__(self, minutes):
        self.hour = (self.hour - ((minutes - self.minute + 59) // 60)) % 24 
        self.minute = (self.minute - minutes) % 60
        return self.__repr__()
