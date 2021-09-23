import random
from collections import Counter # use this :)
two_dices = [random.randint(1,6) + random.randint(1,6) for n in range(20)]
print(two_dices)