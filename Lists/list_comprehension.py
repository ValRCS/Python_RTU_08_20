# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
new_list = []
for num in range(10):
    new_list.append(num*num)
print(new_list)
# list comprehension that does the same as above
squares = [n*n for n in range(10)]
squares

even_squares = []
for num in squares:
    if num % 2 == 0:
        even_squares.append(num)
even_squares
# we can filter using list comprehension
even_squares_2 = [n for n in squares if n % 2 == 0]

# we can filter and make new numbers in the same comprehension
even_squares_3 = [n*n for n in range(10) if n*n % 2 == 0]
even_squares_3

food = "kartupelis"
big_food = [c.upper() * 2 for c in food]
big_food  # this will be a list of mini strings
# how do we get back to string
str(big_food)  # not quite what we need
final_food = "".join(big_food)
final_food

random_list = [1, 2, True, "Valdis", "Peteris", None, 3.167]
int_list = [n*5 for n in random_list if type(n) == int]
int_list
