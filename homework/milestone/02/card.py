from global_libs import card_object

class Card():
    def __init__(self, suit, rank):
        self.suit = suit                #nipe
        self.rank = rank                #card

    def get_value(self):
        return card_object[self.rank]

    def __str__(self):
        return "{} of {}:{}".format(self.rank, self.suit, self.get_value())
        #return self.rank + " of " + self.suit + 

#c = Card(suit='Spades', rank='Two')
#print (c.get_value())
#print (c)