import random
import itertools
  
def get_shuffled_cards():
    suits = ['♥','♠','♣','♦']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = list(itertools.product(suits, values))  # double nested loops
    return random.sample(deck,k=len(deck))
print(get_shuffled_cards())