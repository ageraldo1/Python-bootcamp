import random

deck = set(range(1,53))
hand = random.sample(deck, k=1)
print (hand)
