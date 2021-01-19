# # # using Python standard library
# # # https://docs.python.org/3/library/
# # # Extensive - Batteries Included - just import!
# # # Available across most OSes

# # # 4 ways of importing modules
from datetime import datetime as dt # datetime has datetime submodule!
import string
import math
# # import math as mth # Python likes these short names but not for standard library!
# # from math import floor # i could import floor alone but beware name collission
# from math import factorial as fact
from collections import Counter
from statistics import mean
import random

print(string.punctuation)
before = dt.now()
print(before)
# for i in range(100_000):
#     t = i*3
rand_sum = sum([random.random() for _ in range(100_000)]) # _ because we do not need the variable
after = dt.now()
print(rand_sum/100_000)
print(after)
delta = after - before # so this means time oject have __sub__ overloaded
print(delta)
print(after.year, after.day, after.weekday(), after.hour, after.minute )
print(string.ascii_lowercase)
print(math.factorial(5))
# # print(mth.factorial(4))
# # print(floor(3.98))
# print(fact(6))
my_count = Counter("abracadabra")
# # print(my_count)  # this will be dictionary
print(my_count.most_common())
# # # print(my_count.most_common(3))
# # # # print(my_count.values())
# # # # print(type(my_count.most_common()))
# # # print(my_count['a'])
beg = dt.now()
print(beg)
ran_nums = [random.randint(1, 6)+random.randint(1, 6)
            for _ in range(1_000_000)]
end = dt.now()
print(end)
print(f"Took {end-beg} seconds")
# print(sum(ran_nums)/len(ran_nums))
print(mean(ran_nums))
ncount = Counter(ran_nums)
print(ncount.most_common())
