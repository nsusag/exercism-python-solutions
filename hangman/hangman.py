# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9 
        self.status = STATUS_ONGOING
        self.word = word  
        self.guessed = ['_' for i in range(0, len(word))]

    def guess(self, char):
        if char in self.guessed:
            self.remaining_guesses -= 1
            return
        if self.status != STATUS_ONGOING:
            raise ValueError("The game is already finished.")
        for i in range(0, len(self.word)):
            if char == self.word[i]:
                self.guessed[i] = self.word[i]
        if "".join(self.guessed) == self.word:
            self.status = STATUS_WIN 
        if char not in self.word:
            self.remaining_guesses -= 1
        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        print(self.guessed)

    def get_masked_word(self):
        return "".join(self.guessed)

    def get_status(self):
        return self.status 
