# Arnis
import itertools
import random


def get_card_pack():
    # https://en.wikipedia.org/wiki/Standard_52-card_deck
    value = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    suit = ["♦", "♥", "♣", "♠"]
    pack = list(itertools.product(value, suit))
    return pack


def get_shuffled_cards():
    new_pack = get_card_pack()
    # random.shuffle(new_pack)  # in place
    # return new_pack
    # return random.sample(get_card_pack(), k=52)  # 52 is not cool magic number
    return random.sample(new_pack, len(new_pack))


my_list = get_card_pack()
print(random.choice(my_list))
shuffled_list = random.sample(my_list, k=len(my_list))
print(shuffled_list)
print(my_list)
print(get_shuffled_cards())
