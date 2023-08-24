class Deck():
    '''
    The deck class
    '''

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        '''
        Using the dunder str
        '''
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n '+card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        '''
        Shuffle the deck
        '''
        random.shuffle(self.deck)

    def deal(self):
        '''
        Deal the cards
        '''
        return self.deck.pop()
