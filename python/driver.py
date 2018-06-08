import Deck
#driver.py @baltz_jay 2018

def printDeck(dek):
    for eachCard in range(len(d.deck)):
        print(dek.deck[eachCard].CardToString())

d = Deck.Deck()
print('In order\n')
printDeck(d)

d.shuffle()

print('\nShuffled\n')
printDeck(d)


