import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# list_100_000 = np.random.randint(6, 37, size=100_000).tolist()
list_100_000 = sum([np.random.randint(1, 7, size=100_000) for _ in range(10)])
# print(Counter(list_100_000).most_common())
# print(sorted(Counter(list_100_000).items()))

list_ret = sorted(Counter(list_100_000).items())

names = list(dict(list_ret).keys())
values = list(dict(list_ret).values())

fig, ax = plt.subplots()
ax.bar(names, values)
ax.set_ylim(min(values) - 10, max(values) + 10)

fig.suptitle('2 - 12 -> 100 000')
plt.show()
