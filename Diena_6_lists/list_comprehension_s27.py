my_list = [n for n in range(10)] # could just do list(range(10))
print(my_list)
squares = [n*n for n in range(10)]
print(squares)
even_squares = [n*n for n in range(10) if n%2 == 0]  # so squares for those n who are even (divides by 2 without reminder)
print(even_squares)