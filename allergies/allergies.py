class Allergies:

    def __init__(self, score):
        self.score = score 
        self.allergens = ["cats", "pollen", "chocolate", "tomatoes", "strawberries", "shellfish", "peanuts", "eggs"]

    def allergic_to(self, item):
        return item in self.lst 

    @property
    def lst(self):
        thing = 128 
        result = []
        while self.score > 255:
            self.score -= 256
        for allergen in self.allergens: 
            if self.score >= thing:
                self.score -= thing 
                result.append(allergen)
            thing /= 2
        return result
