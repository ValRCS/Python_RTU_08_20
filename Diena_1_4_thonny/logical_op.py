print(True and True) # True in Python we use and (not &&)
a = 25
b = 10
print("a == 25 and b == 10",a == 25 and b == 10) # if one side is false then everything false
print(a > 5 and b > 20) # if one side is false then everything false
print(True and True and True and False) # one drop of False will ruin everything
print(False and 2*2 == 4 and 3 == 3) # 2*2 == 4 will not be evaluated because False ruined it
print(a >= 5 and b >= 10)
print(a >= 5 and b >= 10 and a > b)
print(a >= 5 and b >= 10 and a < b)
print(False and False) # False
print(True and False) # False
print(False and True) # False
# # # # or (not || in other languages)
# # # one side of or has to be True for the whole expression to be True
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False
# # # with or as soon as one statement is True Python stops evaluation the expression
print("a > 24 or b > 1_000 or 2*2 == 5", a > 24 or b > 1_000 or 2*2 == 5)
print("" or 0 or False)
print(1_000_000 == 1000000 and 1000000 == 1_0_0_0_0_0_0) # last one is NOT recommended
# # 
# # # negation
print(not True)
print(not False)
# # 
print(2 == 3 and 3 == 9000)
print(not 2 == 3) # True
print(not 2 == 3 and 3 == 900) # still False becaue True and False
print(not (2 == 3 and 3 == 900)) # because not otherwise is eval first
# # # 
is_A_over_B = a >= 5 and b >= 10 and a > b
not_so_fast = not is_A_over_B
# #
## Python does not have exclusive or operation (XOR)
# XOR means either of two statements is true but not both
# True XOR True == False
# True XOR False == True
# False XOR True == True
# False XOR False == False
a_xor_b = (a == 25 and b!= 10) or (a != 25 and b == 10)

# and and or priority
# Prioritāte ir NOT, AND, OR :
# https://stackoverflow.com/questions/16679272/priority-of-the-logical-statements-not-and-or-in-python

print(True and True or False and True)
print(False or True and True and True)


# # # # there are also bit operators & and | think ^ and ~
# # # https://realpython.com/python-bitwise-operators/