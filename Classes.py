import random

suits = ('Clubs', 'Spades', 'Hearths', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Cards:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.fulldeck = []
        for rank in ranks:
            for suit in suits:
                self.fulldeck.append(Cards(suit, rank))

    def shuffle(self):
        random.shuffle(self.fulldeck)

    def dealone(self):
        return self.fulldeck.pop()


class Player:

    def __init__(self, name, balance):
        self.playerhand = []
        self.name = name
        self.balance = balance

    def removecard(self):
        return self.playerhand.pop()

    def takefromdeck(self):
        self.playerhand.append(Deck.dealone)

    def __str__(self):
        return f'{self.name} has {len(self.playerhand)} cards'
