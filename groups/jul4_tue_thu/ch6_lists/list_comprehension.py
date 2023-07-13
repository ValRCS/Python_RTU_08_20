# let's talk a little bit about list comprehension
# list comprehension is a way to create a list from some other iterable
# - including another list    

# so we want to create some list of numbers
# we could do it manually like this
square_numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81]
# but what if we want to create a list of squares of numbers from 1 to 100
# we could do it manually but that would be tedious
# we could use a for loop - like this
squares = [] # empty list
for number in range(1, 11): # range is exclusive of the last number
    squares.append(number**2) # we can use ** to raise to power
print(squares)
# we can do the same thing with list comprehension
also_squares = [number**2 for number in range(1, 11)]
# again number is just a name of a variable could be any normal name even n
print(also_squares)
# i could even create 2d lists
# this is a list of lists
# we could use this to create a multiplication table
multiplication_table = [[row*col for col in range(1, 11)] for row in range(1, 11)]
# a bit difficult to read but we can see that we have a list of lists
print(*multiplication_table, sep="\n") # I unrolled the list of lists into individual lists

# again i acced values in 2d list with double indexing
print(multiplication_table[0][0]) # 1
# 3rd row and 5th column
print(multiplication_table[2][4]) # 15
# last row and last column
print(multiplication_table[-1][-1]) # 100

# here it would have been easier to put 0 0 at the start of the list to save on -1 indexing

# list comprehension is a very powerful tool
# we can use it to filter out values from a list
# let's say we want to get only even numbers from our squares list
# we could do it like this
even_squares = []
for number in squares:
    if number % 2 == 0:
        even_squares.append(number)
print(even_squares)

# with list comprehension we can do the previous like this
also_even_squares = [n for n in squares if n % 2 == 0]
# in list comprehension we tend to use shorter variable names
print(also_even_squares)

# so full syntax for list comprehension is
# [expression for item in iterable if condition]

# so let's make a list that contains letter and its corresponding Unicode number
# for Valdis it would be
# [['V', 86], ['a', 97], ['l', 108], ['d', 100], ['i', 105], ['s', 115]]
# we can use ord function to get Unicode number

letter_numbers = [[letter, ord(letter)] for letter in "Valdis"]
print(letter_numbers)

# so when to use list comprehension and when to use for loop
# for loop is more flexible and can do more things 
# use for loop when more logic is needed
# list comprehension is more compact and easier to read