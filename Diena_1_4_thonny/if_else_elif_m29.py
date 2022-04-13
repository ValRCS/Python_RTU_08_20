if False: # after : we always indent
    # start of if block
    print("Do something")
    print("keep doing on True above")
    # in other languages we use {  } Python uses indentation
    # typically 4 spaces, but some like 2, and some 8
# we are out of if block
print("This always runs")
# 
a = 2
b = 4
if a*a == b:
    print(f"{a}*{a} is actually equal to {b}")
    print(a,b)
    # I can keep going
print("Back to always running path")
# 
# # we can make program take ONE of the branches but not both
a = -555
if a > b:
    print(f"{a} is greater than {b}")
    # could do more stuff here
else: # a <= b
    print(f"{a} is less or equal to {b}")
    # could also do more stuff in this path

print("back to main path")
# 
# # we can have more than 2 paths which are exclusive to each other
# # first we can try to catch an error in user input
user_input = input("input a value ")
try: # so similar to if except we check if inside this block we get error
    # i could do more stuff here 
    a = int(user_input)  # try to cast user input to int
except ValueError:  # if something goes wrong we will get to this path
    print(f"You entered something silly -> {user_input}")
    print("so we decided to make a == 0")
    a = 0
#
# a = 4
if a > b:
    print(f"Again {a} is greater than {b}")
    # could do more stuff here
elif a < b:
    print(f"{a} is less to {b}")
else: # only a == b remains
    print(f"Aha! {a} is in fact equal to {b}")
    # do more on this path when a == b
print("Back to main path again")
#

c = 100
# a = 7
if a > b: # outer if
    print("a > b", a, b)
    if c > b:  # nested if inside another if
        print("c > b", c, b)
    else:
        print("c <= b", c, b)
else:
    print("a <= b", a, b)
# # you can do multiple levels of if else
#     