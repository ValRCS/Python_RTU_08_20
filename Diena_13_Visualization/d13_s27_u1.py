from collections import Counter
import matplotlib.pyplot as plt
from random import seed
from random import randrange
import datetime
 
seed(datetime.datetime.now())
data_list = []
for n in range(100_000):
    temp_sum = 0
    for _ in range(6):
        temp_sum += randrange(1,7)
    data_list.append(temp_sum)
#print(Counter(data_list))
my_counter = Counter(data_list)
# x, y = zip(*my_counter.items())
# same as above
x = list(my_counter.keys())
y = list(my_counter.values())

 
plt.bar(x,y)
plt.xlim(6,36)
plt.show() 