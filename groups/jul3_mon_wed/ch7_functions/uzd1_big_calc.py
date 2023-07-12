#1. uzd func
 
def add_mult(a, b, c):
    ordered = sorted([a, b, c])
    return (ordered[0]+ordered[1])*ordered[2]

print(add_mult(2, 7, 3)) # 35
print(add_mult(2, 3, 7)) # 35