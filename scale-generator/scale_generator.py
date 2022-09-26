class Scale:
    def __init__(self, tonic):
        self.tonic = tonic
        self.sharpnotes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        self.flatnotes = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
        self.flatscales = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"] 
        self.sharpscales = ["C", "G", "D", "A", "E", "B", "F#", "a", "e", "b", "f#", "c#", "g#", "d#"]

    def chromatic(self):
        output = []
        if self.tonic in self.flatscales:
            index = self.flatnotes.index(self.tonic)
            for i in range(0, 12):
                output.append(self.flatnotes[(index + i) % 12])
        else:
            index = self.sharpnotes.index(self.tonic)
            for i in range(0, 12):
                output.append(self.sharpnotes[(index + i) % 12])
        print(output)
        return output

    def interval(self, intervals):
        output = []
        if self.tonic in self.flatscales:
            tonic = list(self.tonic)
            tonic[0] = tonic[0].upper()
            tonic = "".join(tonic)
            index = self.flatnotes.index(tonic)
            for char in intervals:
                output.append(self.flatnotes[index % 12])
                if char == "m":
                    index += 1 
                elif char == "M":
                    index += 2
                elif char == "A":
                    index += 3
        else:
            tonic = list(self.tonic)
            tonic[0] = tonic[0].upper()
            tonic = "".join(tonic)
            index = self.sharpnotes.index(tonic)
            for char in intervals:
                output.append(self.sharpnotes[index % 12])
                if char == "m":
                    index += 1 
                elif char == "M":
                    index += 2
                elif char == "A":
                    index += 3
        return output
