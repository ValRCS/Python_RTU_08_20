# we can supply default values for arguments
def add(a, b, c=0, debug=False):
    if debug:
        print("Debugging", a, b, c)
    return a + b + c

# let's call it
print(add(1, 2)) # 3
print(add(1, 2, 3)) # 6
print(add(10, 20, 30, debug=True)) # 60

# it is your responsibility to make sure that the default values make sense
# in other words use sane defaults
