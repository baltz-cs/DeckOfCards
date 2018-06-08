#Card.py @baltz_jay 2018

class Card():
    def __init__(self, face, suit):
        self.face = face        #stored as 0,1,2,3,4,5,6,7,8,9,10,11,12
        self.suit = suit          #stored as 0,1,2,3
        
    def SuitToString(self):
        if self.suit == 0:
            return 'Diamonds'
        elif self.suit == 1:
            return 'Spades'
        elif self.suit == 2:
            return 'Hearts'
        else:
            return 'Clubs'
    def FaceToString(self):
        if self.face == 0:
            return 'Deuce'
        elif self.face == 1:
            return 'Three'  
        elif self.face == 2:
            return 'Four'
        elif self.face == 3:
            return 'Five'
        elif self.face == 4:
            return 'Six'
        elif self.face == 5:
            return 'Seven'
        elif self.face == 6:
            return 'Eight'  
        elif self.face == 7:
            return 'Nine'
        elif self.face == 8:
            return 'Ten'
        elif self.face == 9:
            return 'Jack'
        elif self.face == 10:
            return 'Queen'
        elif self.face == 11:
            return 'King'
        else:
            return 'Ace'  
    def CardToString(self):
        return self.FaceToString() + ' of ' + self.SuitToString()
