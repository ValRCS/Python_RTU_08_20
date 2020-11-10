import itertools
import random
  
def card_mixer():
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♦','♥','♣','♠']
 
    deck_of_cards = list(itertools.product(values, suits))
    return random.sample(deck_of_cards,k=len(deck_of_cards)) # out of place returns new
    # random.shuffle(deck_of_cards) # in place returns None
    # random.sample(deck_of_cards,k=len(deck_of_cards)) # get k samples without replaces
    # return deck_of_cards
    # return random.choice(deck_of_cards)
 
print(card_mixer())