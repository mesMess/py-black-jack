class Chips():
    def __init__(self, current_chips):
        self.total = current_chips  # set to default value/supplied by user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
