# uzd1 VM
from collections import Counter
import random
import matplotlib.pyplot as plt
 
 
ran_nums = [random.randint(1, 6)+random.randint(1, 6)+random.randint(1, 6)+random.randint(1, 6)+random.randint(1, 6)+random.randint(1, 6)
            for _ in range(100_000)]
ncount = Counter(ran_nums)
nc = ncount.most_common()
ran = (len(nc))
x = []
y = []
for i in range(ran):
        x.append(nc[i][0])
        y.append(nc[i][1])
 
plt.bar(x, y)
plt.show()