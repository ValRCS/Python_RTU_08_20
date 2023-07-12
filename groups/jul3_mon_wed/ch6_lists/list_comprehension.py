# let's say we want to get all odd squares of numbers from 0 to 20

squares = []
for number in range(21):
    if number % 2 == 1: # so odd number
        squares.append(number ** 2)

print(squares)

# we could even add number and its square to a list as another list
squares = []
for number in range(21):
    if number % 2 == 1: # so odd number
        squares.append([number, number ** 2])
print(squares)

# so access to last element in a list would be
print(squares[-1])
# how about last lement of last element
print(squares[-1][-1])
# how about first element of last element
print(squares[-1][0]) # 19
# thus we could have multiple levels of nesting - 3D lists, 4D lists, etc.

# we can also use list comprehension to create a list
# list comprehension is a way to create a list from another iterable

# let's create a list of squares of odd numbers from 0 to 20
also_squares = [number ** 2 for number in range(21) if number % 2 == 1]
# number is just a name of a variable - could be anything
print(also_squares)

# i could create a list of unicode values for Valdis
name = "Valdis"
unicode_name = [ord(letter) for letter in name] # so if was optional
print(unicode_name)

# if I did not know about list comprehension I could do it like this
unicode_name = []
for letter in name:
    unicode_name.append(ord(letter))
print(unicode_name)

# i could even make a copy of a list using list comprehension but kind of pointless
numbers = [1,2,3,4,5]
list_copy = [number for number in numbers] # better use numbers.copy()
print(list_copy)
