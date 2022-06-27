# 1. 6 kauliņi
# import random
# import matplotlib.pyplot as plt
# #from collections import count
# # initializing list 
# test_list = [1, 2, 3, 4, 5, 6]
# my_list=[]
# count1=0
# count2=0
# count3=0
# count4=0
# count5=0
# count6=0
  
# for i in range(100000):
#     random_num = random.choice(test_list)
#     my_list.append(random_num)
 
# #how_often=counter(list)
# #print(how_often.most_common())
# for i in range(100000):
#     if my_list[i]==1:
#         count1+=1
#     elif my_list[i]==2:
#         count2+=1
#     elif my_list[i]==3:
#         count3+=1
#     elif my_list[i]==4:
#         count4+=1
#     elif my_list[i]==5:
#         count5+=1
#     else:
#         count6+=1
# library={"1=":count1, "2=":count2, "3=":count3, "4=":count4, "5=":count5, "6=":count6}
# print(library)
# x=test_list
# y=[count1, count2, count3, count4, count5, count6]
# plt.bar(x,y)
# plt.show() 

import matplotlib.pyplot as plt
from collections import Counter
from random import randint
 
DICE = 2
THROWS_MAX = 100_000
throws = [sum(randint(1, 6) for _ in range(DICE)) for each in range(THROWS_MAX)]
throw_counter = Counter(throws)
 
fig = plt.figure()
plt.bar(throw_counter.keys(), throw_counter.values())
plt.show()