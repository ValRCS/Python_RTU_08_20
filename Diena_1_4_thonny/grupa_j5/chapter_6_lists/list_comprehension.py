# list comperehensions in Python

# list comprehensions are a compact way to create lists in Python

# we can use a regular loop
# and create a list
my_list = []
for i in range(10):
    my_list.append(i*3)
print(my_list)

# list comprehensions can do the above in a single line
my_list = [i*3 for i in range(10)] # so loop is inside the []
print(my_list)

# we also have optional if statement

# let's create a list of even numbers
my_list = []
for i in range(10):
    if i%2 == 0:
        my_list.append(i)
print(my_list)

# same thing with list comprehension
my_list = [i for i in range(10) if i%2 == 0]
print(my_list)

# we can modify the element and use if
# and we can create a list of lists
my_even_squares = [[i, i**2] for i in range(10) if i%2 == 0]
print(my_even_squares)

# we can also use nested loops
# and create a list of lists
# lets make a multiplication table
# my_list = []
# for i in range(1,11):
#     for j in range(1,11):
#         my_list.append(i*j)
# print(my_list)

# lets make a 2d list of multiplication table
my_list = [[i*j for j in range(11)] for i in range(11)] # better start with 0 - so index is the number

print(my_list[5][7])
print(my_list[8][9])

print(my_list[0][0])
print(my_list[10][10])

# when do use list comprehensions
# when you want to create a list from another list and logic is simple