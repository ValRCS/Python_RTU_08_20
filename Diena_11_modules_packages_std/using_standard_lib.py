# # # # # using Python standard library
# # # # # https://docs.python.org/3/library/
# # # # # Extensive - Batteries Included - just import!
# # # # # Available across most OSes

# # # # # 4 ways of importing modules
from datetime import datetime as dt # datetime has datetime submodule!
print(dt.now())
# print year, month, day, hour, minute, second
print(dt.now().year)
print(dt.now().month)
print(dt.now().day)
print(dt.now().hour)
print(dt.now().minute)
print(dt.now().second)
# microseconds
print(dt.now().microsecond)

# import string # mostly useful constants
import math
# factorial
print(math.factorial(5))
# # # # # import math as mth # Python likes these short names but not for standard library!
# # # # # from math import floor # i could import floor alone but beware name collission
# # # # from math import factorial as fact
# from collections import Counter # so i only want Counter from collections package
from statistics import mean
# print mean from some numbers
print(mean([1,2,3,4,5,6,7,8,9,10]))
# import random

# import mat_lib # this library comes from my own PYTHONPATH

# print(mat_lib.add(3,76))

# print(string.punctuation)
import random # import should be done before time measurement
before = dt.now()
# print(before) # also printing should be avoided when measuring time
# # for i in range(100_000):
# #     t = i*3

rand_dice = [random.randint(1,6) for _ in range(100_000)] # _ because we do not need the variable
after = dt.now()
print(sum(rand_dice)/100_000)
print(mean(rand_dice))
print(after)
delta = after - before # so this means time oject have __sub__ overloaded
print(delta)
# print(after.year, after.day, after.weekday(), after.hour, after.minute, after.second )
# # # print(string.ascii_lowercase)
# print(math.factorial(5))
# # # # # print(mth.factorial(4))
# # # # # print(floor(3.98))
# # # # print(fact(6))
# Counter can be used to count things
# think of Counter as dictionary with keys and values and some special methods
from collections import Counter
my_count = Counter("abracadabra")
print(my_count)  # this will be dictionary

# i could also count rand_dice
dice_count = Counter(rand_dice)
print(dice_count)
# print(my_count.most_common())
# # # # # # print(my_count.most_common(3))
# print(my_count.keys())
# print(list(my_count.keys()))
# print(my_count.values())

# # # # # # # print(type(my_count.most_common()))
# # # # # # print(my_count['a'])
# beg = dt.now()
# print(beg)
# ran_nums = [random.randint(1, 6)+random.randint(1, 6)
#             for _ in range(1_000_000)]
# end = dt.now()
# print(end)
# print(f"Took {end-beg} seconds")
# print(sum(ran_nums)/len(ran_nums))
# print(mean(ran_nums))
# # so i put all the throws in buckets (presumably from 2 to 12)
# ncount = Counter(ran_nums)
# print(ncount.most_common())


# so key takeaway import only what you need!
# usually IDE will warn you if you import something you do not use
