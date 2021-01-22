import random
from collections import Counter
from matplotlib import pyplot as plt
 
sums=[]
for a in range(0, 100_000):
    total=0
    for b in range(0,6):
        total += random.randint(1,6)
    sums.append(total)
c=Counter(sums)
print(c)
 
plt.bar(c.keys(),c.values())
plt.show()