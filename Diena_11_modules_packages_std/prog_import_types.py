import my_mod
from my_mod import add  # careful of name collissions with other modules
import my_mod as vs_mod
import my_mod as mm
# careful here
# from my_mod import *  # avoid you are polluting global namespace
# print(txt)
# print(mlist)
# add(30, 20)

print(my_mod.add(3, 6))

add2 = my_mod.add

print(add(5, 10))
print(my_mod.add is add)  # so those both point to same function
print(my_mod.add is add2)

print(vs_mod.add(5, 20))
print(my_mod.add is vs_mod.add)  # again we are pointing to the same function
print(mm.add(30, 60))
