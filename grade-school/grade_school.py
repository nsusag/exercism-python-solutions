class School:
    def __init__(self):
        self.students = {} 

    def add_student(self, name, grade):
        self.students[name] = grade

    def roster(self):
        result = []  
        if self.students == {}:
            return result
        for i, member in enumerate(self.students.items()):
            if i == 0:
                minimum = member[1]
                maximum = member[1]
            elif member[1] < minimum:
                minimum = member[1]
            elif member[1] > maximum:
                maximum = member[1]
        for j in range(minimum, maximum + 1):
            for member in sorted(self.students.items()):
                if member[1] == j:
                    result.append(member[0])
        return result  

    def grade(self, grade_number):
        result = []
        for member in self.students.items():
            if member[1] == grade_number:
                result.append(member[0])
        return sorted(result)
        
