class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Invalid value for roll") 
        if len(self.rolls) > 20:
            raise ValueError("Cannot roll after game is finished")
        elif len(self.rolls) == 20:
            if self.rolls[18] + self.rolls[19] < 10:
                raise ValueError("Cannot roll after game is finished")
            elif self.rolls[18] == 10:
                if self.rolls[19] != 10 and self.rolls[19] + pins > 10:
                    raise ValueError("Invalid value for roll")
        currentframe = 1
        currentroll = 1
        for roll in self.rolls:
            if roll == 10:
                currentframe += 1
                currentroll = 1
            else:
                currentroll += 1
                if currentroll == 3:
                    currentframe += 1
                    currentroll = 1
        if currentroll == 2 and self.rolls[-1] + pins > 10:
                raise ValueError("Number of pins in one frame cannot exceed 10") 
        self.rolls.append(pins)

    def score(self):
        currentframe = 1 
        currentroll = 1
        score = 0
        for i, roll in enumerate(self.rolls):
            if currentframe < 10:
                if roll == 10: 
                    score += 10 + self.rolls[i + 1] + self.rolls[i + 2]
                    currentframe += 1
                    currentroll = 0
                elif currentroll == 2:
                    if roll + self.rolls[i - 1] == 10:
                        score += 10 + self.rolls[i + 1]
                    else:
                        score += roll + self.rolls[i - 1] 
                    currentframe += 1
                    currentroll = 0
                currentroll += 1
            else:
                if currentroll == 1 and roll == 10:
                    score += 10 + self.rolls[i + 1] + self.rolls[i + 2]
                    break
                elif currentroll == 2:
                    if roll + self.rolls[i - 1] == 10:
                        score += 10 + self.rolls[i + 1]
                        break
                    else:
                        score += self.rolls[i - 1] + roll
                currentroll += 1
        return score
