import random
import itertools
# from deck_of_cards import deck_of_cards  # pip install deck-of-cards
 
ranks = ("Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King")
suits = ("Clubs", "Diamonds", "Hearts", "Spades")
 
cards = list(itertools.product(ranks, suits))
print("\nKāršu kava:\n", cards)
 
 
def get_shuffled_cards(cards):
    deck = list(cards)
    random.shuffle(deck)
    print("\nSajauktā kāršu kava:\n", deck)
    return deck
 
 
def get_random_sample(cards, count=1):
    card_list = list(cards)
    rs_card = random.sample(card_list, count)
    print("\nKārts no vrknes:\n", rs_card)
    return rs_card
 
 
def get_random_sample_list(cards):
    card_list = list(cards)
    new_deck = random.sample(card_list, len(card_list))
    print("\nJauna sajaukta kāršu kava:\n", new_deck)
    return new_deck
 
 
my_shuffled_cards = get_shuffled_cards(cards)
random_sample = get_random_sample(cards, 10)
get_random_sample_list(cards)

print(my_shuffled_cards[:10]) 

print(random_sample)

print(list(itertools.product(range(5), list("abcd"), ["green", "red"])))