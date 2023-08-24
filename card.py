class Card():
    '''
    This is the card class
    '''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

    def show_card(self):
        '''
        We wanted ten for ten
        '''
