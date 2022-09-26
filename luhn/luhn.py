class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        new_num = []
        for char in self.card_num:
            if not char.isdigit() and not char.isspace():
                return False
            if char.isdigit():
                new_num.append(int(char))
        if len(new_num) < 2:
            return False
        for i, digit in enumerate(new_num[::-1]): 
            if ((i + 1) % 2) == 0:
                if 2 * digit > 9:
                    new_num[len(new_num) - i - 1] = (2 * digit) - 9
                else:
                    new_num[len(new_num) - i - 1] = digit * 2 
        for digit in new_num:
            print(digit)
        return (sum(new_num) % 10) == 0 
