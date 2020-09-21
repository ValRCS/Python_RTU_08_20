# Sajaukums
# uzrakstiet funkciju get_shuffled_cards():
# Funkcijas iekšpusē Izveidojiet 52 kāršu virkni  [("2", "kāravs"),("2", "ercens"),..... ,("A", "kreics"),("A", "pīķis")]
# Funkcija atgriež sajauktu kāršu komplektu - tas pats lists ar tuples iekšpusē derēs
# Paši nejauciet, izmantojiet jau gatavo!
# standarta bibliotekā random sadaļā
# atrodiet izvēles funkciju, kas atgriež patvaļīgu kārti no virknes.
# atrodiet sajaukšanas funkciju (in place!)
from random import sample
import random
kartis = []


def get_shuffled_cards():
    zimes = ["kāravs", "pīķis", "ercens", "kreicis"]
    for i in range(2, 15):
        for j in range(0, 3):
            if i == 11:
                k = "A"
            elif i == 12:
                k = "D"
            elif i == 13:
                k = "K"
            elif i == 14:
                k = "T"
            else:
                k = i
            paris = [k, zimes[j]]
            kartis.append(paris)
    # return kartis
    return(sample(kartis, len(kartis)))


print(get_shuffled_cards())
print(random.choice(kartis))

print(sample(range(10000000), k=10))
