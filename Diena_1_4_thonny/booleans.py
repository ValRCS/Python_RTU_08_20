is_raining = False
is_sunny = True
is_summer = False
# # # # false = True # legal name for variable but not not recommended...
# # # # False = False # not legal at all,
print(is_raining, is_sunny)
print(type(is_raining), type(is_sunny), type(is_summer))
print(2 * 2 == 4)  # notice  double == , this is comparison this is not assignment!
print(2 * 2 == 5)
# # # # # # #
# # # # # 
is_math_correct = 2 * 2 == 4  # we go from right to left
# # # # # #
print("Is math still correct?",is_math_correct)
# # # # # more often we would use variables in at least one side of comparison
a = 2
b = 4
print(a * a == b, a * a == 4, a * a == 5)  # more common
print(2 == 2.0)  # two types but should be true
print(1 == True, True == 1, False == 0, 0 == False)  # True is represented by 1, we should actually use is to compare with False and True
print(3 == True)  # 3 is truthy but not True
a = True  # changing data type from int to bool here (generally avoid)
print("a is ", a)
print(1 == a)
# # # # 
# # # # print(0 == a)
# # # # print(3 == a) 
# # # # These kind of tricks best be avoided
print(True+True+True+False+True) # so 4 because this is just regular math with 1 and 0
# # # # # # # # and False by 0
# # # # # # # # there are some other falsy values, meaning values which equal to False when comparing
print("" == False)  # empty string is not the same as False but it will be used similarly in logical operations
print("" == '')  # True because it is same empty string
my_name = "Valdis"
print(my_name == my_name, my_name == "Valdis", my_name == "Voldis")
print("Valdis" == 55)
print(my_name == 55)
# # # # # # #
# # # # # # # # inequality
a = 2
b = 4
print(a != b)  # if they are inequal then != will give True
print(2 != 2)  # this is a False statement because 2 is in fact equal to 2
is_equal = a*2 == b # evaluation is from right side then assignment
is_not_equal = a * 2 != b
print(is_equal, is_not_equal)
is_not_equal = a * 5000 != b / 1541
print(is_not_equal)
# # # # 
print(0.1 + 0.2 == 0.3) # careful here !! floating points
print(0.1 + 0.2)
my_round = round(0.1 + 0.2, 4) # 4 digits after comma
print(my_round)
print(round(0.1+0.2, 4) == round(0.3, 4))
# # # print(my_round == round(0.1+0.2, 4))
# # # # # #
print(a * 5 == b * 2.5)
a = 10
b = 20
print(a * 5 == b * 2.5)
# # a = 15
# # print(a * 5 == b * 2.5)
# # # # # # #
# # # # # # # # greater >
print(2 > 3, 3 > 2, 9001 > 9000)
print(a * a > 3, a * a > b, a * a > 5, a * a > b * 15)
# # b = 10
# # print(a * a > 3, a * a > b, a * a > 5, a * a > b * 15)
print(True > False)  # if True is 1 and False is 0 then this should be True :)
# # # # # # # # we can compare other data types
print("Voldemars" > "Valdis")  # gives us True but why?
# # # # # # # #
print("Voldis" > "Valdis")  # this is also true
print("Vol" > "Valdis")
print(ord("V"), ord("a"), ord("o"), ord("ā"), ord("@"), ord("😅")) # we can get Unicode codes for characters
print(chr(86), chr(97), chr(257), chr(8000), chr(8364), chr(128517))  # i can print from codes the symbols
# # # # # #
# # # # # # # if we need by length - we can measure length of sequences , strings and many other types
print(len("Voldemārs") > len("Valdis"))
print(len("Voldemārs"))
print(len("Valdis"))
# # # # # # # less than <
print(2 < 3, 3 < 3, a < b, b < a)
# # # # # # #
# # # # # # # # less or equal
print(2 <= 3, 3 <= 3, 3 <= 4, 5 <= 3)
a=15
print(a <= 14, a <= 15, a <= 16)
# # # # # # #
# # # # # # # # gt greater or equal
print(2 >= 3, 3 >= 3, 4 >= 3, a * 4 >= b * 3)  # => not possible
# # # # # # #
# # # # # #
# # 
b = 20
c = 50
print(a,b,c,1000)
# # i can compare multiple values at once without AND
print(a < b < c < 1000)  # a is still 15 here so this will be false
b = -33
print(a < b < c < 1000) # now b ruined our True statement into False
# # # a = 8
# # # # # # we can compare more than two at once
# # # print(a,b,c,1000)
# # # print(a < b < c < 1000)  # four values at once
# # # # print(a < -50 < b < c < 1000)  # false because first operation shortcircuits to False
# # # # # # #
# # # # print(-50 < a < b < c < 1000)
# # # # # # # # is compares actual memory address
# # # # # # # # used less
print(a is b)  # really it is id(a) == id(b)
# # print(2 is 2)  # should not really use instead use == AVOID!
# print(2*2 == 4 is True) # use to compare something with True or False
# print((2*2 == 4) is True) # turns out is is more important than ==
print(is_math_correct is True)
# # # print(True is True)
# # # # # # # # we use it when we need to see if both variables point to same object
# # # # # # # is can be handy for finding whether you have same shopping cart
# # # # # # or you have two different shopping carts with same items - just an analogy
a = 8
b = 10
print(a + b == c - 32, a + b == c + 1 - 32)
print("All Done")
# # # # # 