import ast
t = input("input dict { }")
d = ast.literal_eval(t)  # should work with all kind of basic data types
print(d, type(d))
