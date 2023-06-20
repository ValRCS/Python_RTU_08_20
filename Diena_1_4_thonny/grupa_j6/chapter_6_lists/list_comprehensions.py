# list comprehensions in Python are a concise way to create lists
# also they provide a way to transform lists
# and filter them

# let us create a list of squares
squares = []
for i in range(10):
    squares.append(i**2) # so squares of the numbers
print(squares)

# we can rewrite this using list comprehension
squares = [i**2 for i in range(10)]
# list comprehensions are a little bit faster than regular for loops

# we can also use if statements in list comprehensions
# let us create a list of even numbers
even_numbers = []
for i in range(10):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)

# we can rewrite this using list comprehension
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# we can also use if else statements in list comprehensions
# let us create a list of even numbers and odd numbers
even_odd_numbers = []
for i in range(10):
    if i % 2 == 0:
        even_odd_numbers.append("even")
    else:
        even_odd_numbers.append("odd")

print(even_odd_numbers)

# we can rewrite this using list comprehension
even_odd_numbers = [f"even {i}" if i % 2 == 0 else f"odd {i}" for i in range(10)]

print(even_odd_numbers)

# in practice use list comprehensions when you have simple for loops
# for more complicated logic  loops use regular for loops