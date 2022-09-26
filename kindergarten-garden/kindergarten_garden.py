class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.diagram = diagram
        self.students = students 
    def plants(self, student): 
        index = 0 
        for member in self.students:
            if member < student:
                index += 1
        result = []
        for char in [self.diagram[index * 2], self.diagram[index * 2 + 1], self.diagram[index * 2 + int((len(self.diagram) + 1) / 2)], self.diagram[index * 2 + int((len(self.diagram) + 1) / 2) + 1]]: 
            if char == 'C':
                result.append("Clover")
            elif char == 'G':
                result.append("Grass")
            elif char == 'R':
                result.append("Radishes")
            elif char == 'V':
                result.append("Violets")
        return result
