# lists are the most versatile of Python's compound data types. 
# We use lists to hold an ordered sequence of values.

# let's see what happens if we do not have a list
xyz1 = 1
xyz2 = 20
xyz3 = 300
xyz4 = 4000
xyz5 = 50000
print(xyz1, xyz2, xyz3, xyz4, xyz5)
# how about if we need more variables?
# 20 variables? 100 variables? 1000 variables?
# as soon as we have more than 2 similar variables, we should use a list
# other languages call this an array

# let's create a list
# empty list
my_list = []
print(my_list)

# we can append to the end of a list
my_list.append(10) 
# append is IN PLACE - means it changes the list !!!
print(my_list)
my_list.append(20)
print(my_list)
# Python lists let us mix different types of data
my_list.append("hello")
my_list.append(3.14)
my_list.append(True)

# let us go through the list and print each element and type
for element in my_list:
    # print(element, type(element))
    print(f"Element {element} {type(element)}")

# we can also create a list with initial values
numbers = [1, 2, 3, 4, 5]
# for more numbers we can use list with range
big_numbers = list(range(100,120))

# i can create a list from a string
my_string = "Hello World"
my_list = list(my_string)
print(my_list)
# lists are mutable - we can change them
my_list[3] = "XX"

# to remove elements we have several options
print(numbers)
# remove by value
numbers.remove(3) 
# remove by index
del numbers[1] # removed second element
# remove last element
last_number = numbers.pop() # most efficient from end
# pop returns the value of the element removed
print(numbers)
print(last_number)

# again remove and pop are IN PLACE - means they change the list !!!

# if we have a list of strings we might want to combine them
# into a single string
my_list = ["Hello", "World", "Python"]
my_string = str(my_list) # most likely not what we want
print(my_string)
# we can use join
my_string = " ".join(my_list) # so we use a space to join
print(my_string)
# i can use any string(emoji etc) to join or even empty string
my_string = "👍".join(my_list)
print(my_string)
my_string = "".join(my_list)
print(my_string)
# lets go back to space
my_string = " ".join(my_list)
print(my_string)

# we might want to split a string into a list
# by default split uses whitespace to split
new_list = my_string.split()
# i could use any string to split
another_list = my_string.split("o")

# all the slicing and indexing methods we used with strings work with lists

# how about every 2nd element in big_numbers
print(big_numbers[::2])
# how about reverse order
print(big_numbers[::-1])
# how about from 3rd to 7th element use zero based indexing
print(big_numbers[2:7])

