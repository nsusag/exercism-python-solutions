import random

class Character:
    def __init__(self):
        results = []
        for i in range(0, 6):
            dicerolls = []
            for i in range(0, 4):
                dicerolls.append(random.randint(1, 6))
            print(sorted(dicerolls))
            results.append(sum(sorted(dicerolls)[1:])) 
        self.strength = results[0]
        self.dexterity = results[1]
        self.constitution = results[2]
        self.intelligence = results[3]
        self.wisdom = results[4]
        self.charisma = results[5]
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        ability = random.randint(1, 6)
        if ability == 1:
            return self.strength
        elif ability == 2:
            return self.dexterity    
        elif ability == 3:
            return self.constitution
        elif ability == 4:
            return self.intelligence
        elif ability == 5:
            return self.wisdom
        elif ability == 6:
            return self.charisma

def modifier(constitution):
    return (constitution - 10) // 2
