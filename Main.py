from Classes import Player, Deck, Cards

game = True
dealer = Player('Dealer', 0)
player = Player('Player', 1000)

newdeck = Deck()
newdeck.shuffle()
''''
print(len(newdeck.fulldeck))
print(newdeck.fulldeck[0])
'''


def turn():
    dealer.playerhand.append(Deck.dealone)

    print(len(dealer.playerhand))



turn()
print(len(newdeck.fulldeck))
"""

while game:

    if len(Classes.Deck().fulldeck) == 0:
        newdeck = Classes.Deck()
        newdeck.shuffle()

"""
