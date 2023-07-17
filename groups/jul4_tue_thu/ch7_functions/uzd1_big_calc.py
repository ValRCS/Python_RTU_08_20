# --- 2.1 Uzdevums ---
#----------------------
def add_mult(a, b, c):
    arguments = [a, b, c]
    arguments.sort()
    result = (arguments[0] + arguments[1]) * arguments[2]
    return result

# tests
print(add_mult(2, 3, 4)) # 20
print(add_mult(4, 3, 2)) # 20

assert add_mult(2, 3, 4) == 20
assert add_mult(4, 3, 2) == 20
assert add_mult(0,5,0) == 0
assert add_mult(-5,-2,-3) == 16