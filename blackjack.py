import random
# import deck
# import chips


'''
This is a simple game of blackjack I based it
on a game I downloaded from the app store
'''

'''Missing features:
1) Players class implementation and use
2) Chips totals carried over (complete)
3) Chips totals based on Players (complete)
4) Show chips totals on screen'''

SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


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


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += VALUES[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():
    def __init__(self, current_chips):
        self.total = current_chips  # set to default value/supplied by user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


class Player():
    # Needs to be implementated...
    def __init__(self):
        self.hand = player_hand
        self.chips = player_chips


def take_bet(chips):
    '''
    Take_Bet
    '''
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            elif chips.bet == 0 or chips.bet < 0:  # fix
                print('Sorry, your bet cannot be less than or equal to zero')  # fix
            else:
                break


def hit(deck, hand):
    '''
    Hit me
    '''
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    '''
    hit or stand allows you to hit to take another card
    or stand to stop a round
    '''
    global playing  # to control an upcoming while loop

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck, hand)  # hit() function defined above
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    # chips.lose_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    # chips.win_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


player_chips = None

# Game loop
while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11.')

    # Create & shuffle the deck
    deck = Deck()
    deck.shuffle()

    # Deal two cards to each player
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    if player_chips is None:
        starting_chips = int(input('How many chips do you want? '))
        player_chips = Chips(starting_chips)
    elif player_chips.total == 0:
        player_chips.total = int(input('It\'s time for more chips: '))  # fix
    else:
        pass

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If player hasn't busted, play Dealer's hand until Dealer Reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
            player_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
            player_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
            dealer_busts(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    print("\nPlayer's winnings stand at", player_chips.total)

    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game.lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!!")
        break
