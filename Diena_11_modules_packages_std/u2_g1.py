import itertools
import random
from random import shuffle
 
def set_card_pack():
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]
    suits = ["♣", "♦", "♥", "♠"]
    card_pack = list(itertools.product(ranks, suits))
    return card_pack
 
def get_shuffled_card_pack():
    new_card_pack = set_card_pack()
    return random.sample(new_card_pack, k=52)
 
def main():
    random.seed(42)
    my_pack = set_card_pack()
    # print(my_pack)
    # print()
 
    print(random.choice(my_pack)) # we keep cards
    shuffled_card_pack = get_shuffled_card_pack()

    print(shuffled_card_pack.pop()) # so only 51 cards in the pack
    print(len(shuffled_card_pack))
    # print(get_shuffled_card_pack())
 
if __name__ == "__main__":
    main()