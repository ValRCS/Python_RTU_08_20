# Python has  rich standard library with many modules and packages
# full docs: https://docs.python.org/3/library/index.html

# we saw using sys to print Python version
import sys
print(f"Python version: {sys.version}")

# we saw math module
import math
print(f"math.pi: {math.pi}")
# sinus
print(f"math.sin(math.pi / 2): {math.sin(math.pi / 2)}")

# we saw statistics module
import statistics
data = [1, 2, 3, 4, 5]
print(f"statistics.mean(data): {statistics.mean(data)}") # 3.0
#there is median function in statistics module
print(f"statistics.median(data): {statistics.median(data)}") # 3
# and others

# there there is datetime module
# import datetime
# # this has a slightly unfortunate name
# # we typically want datetime class from datetime module
# # so now would be
# now = datetime.datetime.now()
# print(f"now: {now}")

# so it is often better to import datetime class from datetime module
from datetime import datetime # now I can use datetime class directly
now = datetime.now()
print(f"now: {now}")

# we saw collections module which has Counter class
from collections import Counter
food_list = ['pizza', 'pasta', 'sushi', 'ramen', 'tacos', 'pizza', 'sushi', 'sushi']
food_counter = Counter(food_list)
print(f"food_counter: {food_counter}")

# key point all of this is included in Python standard library
# you just pick what you need and use it