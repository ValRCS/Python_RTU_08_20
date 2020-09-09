print(True and True) # in Python we use and (not &&)
a = 25
b = 10
print(a > 5 and b > 20) # if one side is false then everything false
print(True and True and True and False)
print(a >= 5 and b >= 10)
print(a >= 5 and b >= 10 and a > b)
print(False and False)
print(True and False)
print(False and True)
# or (not || in other languages)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(a > 34 or b > 1_000)
print("" or 0 or False)
print(not True)
isAoverB = a >= 5 and b >= 10 and a > b
notSoFast = not isAoverB
# there are also bit operators & and | and i think ^ and ~