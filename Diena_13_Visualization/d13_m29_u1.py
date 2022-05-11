# Task 1
 
# import matplotlib.pyplot as plt
# import random
# from collections import Counter
 
# dicerolls = 100_000
# dices = 3
 
# results = [0]*dicerolls
# for diceroll in range(dicerolls):
#     for dice in range(dices):
#         results[diceroll] += random.randint(1,6)
 
# freq = Counter(results)
 
# plt.bar(freq.keys(), freq.values())
# plt.xlabel(str(dices) + " kauliņu summa")
# plt.ylabel("Biežums")
# plt.show()

import random
from collections import Counter
from tqdm import tqdm # tqdm: A Fast, Extensible Progress Bar for Python
from matplotlib import pyplot as plt
 
shots = 1_000_000
throws = 6
result=[]
for i in tqdm(range(shots)):
    sum=0
    for j in range(throws):
        sum += random.randint(1,6)
    result.append(sum)
count=Counter(result)
 
plt.bar(count.keys(), count.values())
plt.ylabel("Shots")
plt.title("Sum of six shots")
plt.show()