# 1 uzd
 
import random
from collections import Counter
from matplotlib import pyplot as plt
 
sums=[]
tries = 1_000_000
dice_count = 6
for a in range(tries):
    total=0
    for b in range(dice_count):
        total += random.randint(1,6)
    sums.append(total)
c=Counter(sums)
print(c)
 
plt.bar(c.keys(),c.values())
plt.show()