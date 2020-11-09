import u2_g1 as crds
from u2_g1 import get_shuffled_card_pack as get_shuffled_cards

cards = crds.get_shuffled_card_pack()
print(cards[:5])
pack_2 = get_shuffled_cards()
print(pack_2[:5])