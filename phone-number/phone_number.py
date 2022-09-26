class PhoneNumber:
    def __init__(self, number):
        acceptables = [" ", "(", ")", ".", "-", "+"] 
        cleaned = []
        for char in number:
            print(char)
            if char.isdigit():
                cleaned.append(char) 
            elif char not in acceptables:
                raise ValueError("Invalid character in number")
        print(cleaned)
        if len(cleaned) == 11:
            if cleaned[0] != "1":
                raise ValueError("Country code is not 1")
            cleaned = cleaned[1:]
        if len(cleaned) == 10:
            if int(cleaned[0]) < 2 or int(cleaned[3]) < 2:
                raise ValueError("Area code or number starts with wrong digit")
        else:
            raise ValueError("Length of number is wrong")
        self.number = "".join(cleaned)
        self.area_code = self.number[0:3]
    def pretty(self):
        output = ["(", self.number[0:3], ") ", self.number[3:6], "-", self.number[6:]]
        return "".join(output)
