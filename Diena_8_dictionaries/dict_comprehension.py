# Dictionary Comprehension
# https://www.python.org/dev/peps/pep-0274/
my_squares = {str(n): n*n for n in range(5)}
print(my_squares)


squares = {}
for n in range(5):
    squares[str(n)] = n*n
print(squares)

my_cubes = {f"Cube of {n}": n**3 for n in range(8)}
print(my_cubes)
food = "kartupelis"
abc = "abcdefghij"
cypher = {k: v for k, v in zip(food, abc)}
print(cypher)
abc_dict = {v: i for i, v in enumerate(abc, start=1)}
print(abc_dict)
zero_dict = {c: 0 for c in food}
print(zero_dict)
