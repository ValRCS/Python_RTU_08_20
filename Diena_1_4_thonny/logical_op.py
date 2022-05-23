# # logical negation # in Python we use not (not ! as in many other languages)
print(not True)
print(not False)
is_sunny = False
print(is_sunny)
is_sunny = not is_sunny # Toggle my truth value
print(is_sunny)
is_sunny = not is_sunny # Toggle my truth value
print(is_sunny)
# # 
# # # logical conjunction
print(True and True) # True in Python we use and (not &&)
print(True and False) # False
print(False and True) # False
print(False and False) # only True and True is True
a = 5
b = 10
print("a == 5 and b == 10",a == 5 and b == 10) # if one side is false then everything false
print(a > 2 and b > 20) # if one side is false then everything false
# 
print(2 < a < b )
print(2 < a and a < b) # same as previous line
print(2 < a < b < 100)
print(2 < a and a < b and b < 100) # same as above line
print(True and True and True and False) # one drop of False will ruin everything
# # these statements are lazily evaluated Python stops when everything is clear
# 
print(False and 2*2 == 4 and 3 == 3 and 5/0==10000) # 2*2 == 4 will not be evaluated because False ruined it
# print(True and 2*2 == 4 and 3 == 3 and 5/0==10000) # 2*2 == 4 will not be evaluated because False ruined it
divider = 20
print(divider != 0 and 100 / divider == 5)
# # # print(a >= 5 and b >= 10)
# # # print(a >= 5 and b >= 10 and a > b)
# # # print(a >= 5 and b >= 10 and a < b)
# # # print(False and False) # False
# # # print(True and False) # False
# # # print(False and True) # False
# 
# # # Logical Disjunction
# # # # # # # # or (not || in other languages)
# # # # # # # one side of or has to be True for the whole expression to be True
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False
# # # # # # # with or as soon as one statement is True Python stops evaluation the expression
print("a > 4 or b > 1_000 or 2*2 == 5", a > 4 or b > 1_000 or 2*2 == 5)
# print("" or 0 or False)
print(1_000_000 == 1000000 and 10_00000 == 1_0_0_0_0_0_0) # last one is NOT recommended
# # # # # # 
# # # # # # # negation
# # # print(not True)
# # # print(not False)
# # # # # # 
# # # print(2 == 3 and 3 == 9000)
# # # print(not 2 == 3, 2 != 3) # True
# # # print(not 2 == 3 and 3 == 900) # still False becaue True and False
# # # print(not (2 == 3 and 3 == 900)) # because not otherwise is eval first
# # # # # # # 
# # # is_A_over_B = a >= 5 and b >= 10 and a > b
# # # not_so_fast = not is_A_over_B
# # # # # #
# # # # ## Python does not have exclusive or operation (XOR)
# # # # # XOR means either of two statements is true but not both
# # # # # True XOR True == False
# # # # # True XOR False == True
# # # # # False XOR True == True
# # # # # False XOR False == False
# # # so XOR is true when just one statement is True
# a = 25
a_xor_b = (a == 25 and not b == 10) or (not a == 25 and b == 10)
print(a_xor_b)
# # # # 
# # # # # and and or priority
# # # # # Prioritāte ir NOT, AND, OR :
# # # # # https://stackoverflow.com/questions/16679272/priority-of-the-logical-statements-not-and-or-in-python
# # # # 
# # # # print(True and True or False and True)
# # # # print(False or True and True and True)
# # # # 
# # # # 
# # # # # # # # there are also bit operators & and | think ^ and ~
# # # # # # # https://realpython.com/python-bitwise-operators/
print(bin(3))
print(bin(4))
print(bin(255)) # 128+64+32+16+8+4+2+1
print(bin(253)) # 128+64+32+16+8+4+0+1
# print(bin(127))
print(bin(5), bin(6), bin(5 & 6), 5 & 6, sep="\n") # so bit wise and
print(bin(5), bin(6),  bin(5 | 6), 5 | 6, sep="\n")
# # # so bit wise or
# # # there is bitwise xor
print(bin(5), bin(6),  bin(5 ^ 6), 5 ^ 6, sep="\n")