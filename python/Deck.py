import Card

import random
#Deck.py
class Deck(object):
    global deck
    deck = []
    def __init__(self,deck =[]):
        self.deck = deck
        for faces in range(13):
            for suits in range(4):
                self.deck.insert(0, Card.Card(faces, suits))
    def __getitem__(self, index):
        return self.deck[index]
    def pop(self, index = 0):
        return self.deck.pop(index)
    def shuffle(self):
        random.shuffle(self.deck)
