SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J K A'.split()

# mycards = [(s, r) for s in SUITE for r in RANKS]

# we can write like this too
"""
mycards = []
for r in RANKS:
    for s in SUITE:
        mycards.append(s, r)
"""


class Deck:
    """ This is Deck Class. This object will create a deck of cards to
        initiate play. """
    def __init__(self):
        print("Creating new Ordered Deck!")
        mycards = []

        for r in RANKS:
            for s in SUITE:
                mycards.append(s, r)

        return mycards
        self.allcards = mycards

        def shuffle(self):
            print("SHUFFLING DECK")
            shuffle.allcard

        def split_in_half(self):
            return (self.allcards[:26], self.allcards[26:])

    class Hand:
        """ This is a habd class. Each playesrs has hands"""
        def __init__(self, cards):
            self.cards = cards

        def __str__(self):
            return "Contains {} cards".format()(len(self.cards))

        def add(self, added_cards):
            self.cards.extend(added_cards)

        def remove_card(self):
            return self.cords.pop()


class Player:
    """
    This is the Player Class, which takes in a name an
    instace of a hand class objects.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        for x in range(3):
            war_cards.append(self.hand.card.pop())
        return war_cards

    def still_has_cards(self):
        """
        Return True if player has cards.
        """
        return len(self.hand.cards) != 0

    print("Welcome to war, let's begin...")

    d = Deck()
    d.shaffle()
    half1, half2 = d.split_in_half()
