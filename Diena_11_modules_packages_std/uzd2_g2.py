# Vitauta risinājums
import itertools
import random


def get_52_cards():
    l = '2 3 4 5 6 7 8 9 10 J Q K A'.split(" ")
    s = '♦ ♥ ♣ ♠'.split(" ")
    return list(itertools.product(l, s))  # Cartesian Product


def get_shuffled_card(list_52):
    random.shuffle(list_52)  # in place
    return random.choice(list_52)


def get_shuffled_cards(list_52, _int):
    random.shuffle(list_52)
    return random.choices(list_52, k=_int)


def main():
    # print(get_52_cards())
    print(get_shuffled_card(get_52_cards()))
    print(get_shuffled_cards(get_52_cards(), 3))
    print(get_shuffled_cards(get_52_cards(), 7))


if __name__ == "__main__":
    main()
    # ko darīt ja šo failu neimportē bet izsauc pa tiešo
