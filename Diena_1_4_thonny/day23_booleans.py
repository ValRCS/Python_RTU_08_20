# Boolean data type
is_sunny = False # notice capitilized
is_spring = True
print(is_sunny, is_spring)
# we can get Booleans from comparision operators
print(2 < 3)
print(2*2 == 4)
print(2+2 == 5)
# notice == not =
# assignment with =
result = 2*2
# comparision with ==
# evaluation happens form right to left
are_equal = 2*2 == 4
print(result, are_equal)
# it is possible to make a do nothing line
result == 10*10 # we compare 100 with result and it is False
# but nothing is done
# we probably wanted
result = 10*10
# a = int(input("Enter an integer please"))
# b = int(input("Enter another integer"))
# is_a_lt_b = a < b # again from right side to left
# print(f"{a} is less than {b} ? {a < b} {is_a_lt_b}")
# we have loose inequality
print(2 <= 3, 3 <= 3, 3 <= 2)
print(2 >= 3, 3 >= 3, 3 >= 2)

# inequality !=
print(2 != 2) # False
print(2*2 != 4) # still False
print(2 != 3) # True
# again at least one side will be a variable
# otherwise these are constants