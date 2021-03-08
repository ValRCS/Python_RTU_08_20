import random, itertools
 
# def generate_cards():
#     card_pack = []
#     card_nominals = ["kāravs", "ercens", "kreics", "pīķis"]
#     card_pictures = ["J", "Q", "K", "A"] # šeit var vē jokerus pielikt klāt
#     for number in range(2, 11):
#         for i in card_nominals:
#             card_pack.append((f"{number}", i))
#     for pict in card_pictures:
#         for nom in card_nominals:
#             card_pack.append((pict, nom))
#     return card_pack
 
# def get_shuffled_cards():
#     new_pack = generate_cards()
#     random.shuffle(new_pack)
#     return new_pack
 

def get_shuffled_cards():
    h = list(range(2,11)) + ["Ace", "King", "Queen", "Jack"]
    # h.append("Ace")
    # h.append("King")
    # h.append("Queen")
    # h.append("Jack")
    deck = list(itertools.product(h,['of ♣','of ♦','of ♥','of ♠'], ))
    random.shuffle(deck) # in place
    return deck
 
# print(get_shuffled_cards())
# print(random.choice(get_shuffled_cards()))

if __name__ == "__main__": 
    # print(generate_cards)
    # print(get_shuffled_cards())
    shuffled_deck = get_shuffled_cards()
    print(shuffled_deck)
    last_card = shuffled_deck.pop() # so we can start playing pigs
    print(last_card)
