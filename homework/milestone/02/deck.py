import random
from global_libs import card_object, suits
from card import Card

class Deck():
    def __init__(self, decks=1):
        self.deck = []
        self.number_decks = decks

    def prepare_deck(self):
        self.deck.clear()

        for _ in range(self.number_decks):
            for suit in suits:
                for rank in card_object.keys():
                    self.deck.append(Card(suit, rank))

        self.shuffle()

    def __str__(self):        
        return ",".join([str(self.deck[x]) for x in range(0, len(self.deck))])
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self, total_cards=1):
        return ([self.deck.pop() for _ in range(total_cards)])

#d = Deck()
##d.prepare_deck()
#print ("Deck size : {}".format(len(d.deck)))
#for card in d.deal(2):
#    print ("\t{}".format(card))
#print(d.pick_card(2)[0])
#print ("Deck size : {}".format(len(d.deck)))


#print ("\t{}".format(str(d.deal()[0])))



