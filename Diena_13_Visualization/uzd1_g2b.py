# Maijas
import matplotlib.pyplot as plt
import random
from collections import Counter
kaulinu_summa = [sum([random.randint(1, 6), random.randint(1, 6), random.randint(
    1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]) for i in range(100_000)]
counter = Counter(kaulinu_summa)

plt.bar(counter.keys(), counter.values())
plt.show()
