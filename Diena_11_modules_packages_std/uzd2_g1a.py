# Antras
import itertools
import random


def card_mixer():
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']

    deck_of_cards = list(itertools.product(values, suits))

    # changes the original list
    random.shuffle(deck_of_cards)

    # returns random tuple from list
    return random.choice(deck_of_cards)


print(card_mixer())
