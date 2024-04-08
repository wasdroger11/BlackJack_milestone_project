from Classes import Player, Deck

game = True
betamount = 0
dealer = Player('Dealer', 0, 0)
player = Player('Player', 1000, 0)
newdeck = Deck()
newdeck.shuffle()


def bet():
    global betamount
    intcheck = False
    while not intcheck:
        betamount = input("How much would you like to bet?")
        if betamount.isdigit():
            if int(betamount) > player.balance:
                print("You do not have enough funds for that bet")
            player.balance = player.balance - int(betamount)
            print(f'You have placed a bet of ${betamount}')
            intcheck = True


def balance():
    print(f'You have ${player.balance} left in your account')


def turn():
    global newdeck
    if len(newdeck.fulldeck) == 0:
        newdeck = Deck()
        newdeck.shuffle()
        print('A new deck of cards has been added to the pack')
    dealer.playerhand.append(newdeck.dealone())
    player.playerhand.append(newdeck.dealone())
    print(f'The dealer has received a {dealer.playerhand[-1]}')
    print(f"The dealer's count is  {player.totalvalue()}")
    print(f'You have received a {player.playerhand[-1]}')
    print(f'Your count is  {player.totalvalue()}')


bet()
'''
while game:
    if len(Deck().fulldeck) == 0:
        newdeck = Deck()
        newdeck.shuffle()
    if player.totalvalue() > 21:
        pass
'''
