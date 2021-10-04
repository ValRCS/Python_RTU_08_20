# # # # # a = 215
# # # # a = int(input("Input a"))
# # # a = 9000
# # # a = 3
# # #
# if True:
#     print("This always runs because if statement is True")
#     print("Still working in if block")
# # #
# # # # # after we go back to our normal indentation the if block is ended
# # # #
a = 5
# if a > 10: # in Python when you see : next line will be indented
#     # runs only when statement after if is True
#     print("Do this when a is larger than 10")
#     print("Still only runs when a > 10", a)
#     # we can keep doing things when a > 10 here
# # #
# # # # # here we have exited if
# print("This will always print no matter what")
# # # # # # # #
# # # # # # #
# # # # # # a = -333
# # # # # # a = 200
# a = 44
# # # a = 10
# # if a > 10:  # in Python when you see : next line will be indented
# #     # runs only when statement after if is True
# #     print("Again Do this when a is larger than 10")
# #     print("Indeed a is", a)
# # else:  # when a is <= 10
# #     print("Only when a is less or equal to 10")
# #     print("Indeed a is only", a)
# #     # we could do more stuff here when a is not larger than 10
# # # #
# # # # # # a = 10
# # a = 200
# # # # a = -95
# a = 10
# # a = -355
# # if we need more than 2 distinct paths
# if a > 10:  # in Python when you see : next line will be indented
#     # runs only when statement after if is True
#     print("Again Do this when a is larger than 10", a)
# elif a < 10:
#     print("ahh a is less than 10", a)
# else:  # so a must be 10 no other choices you do not need to check, after all other choices are exhausted
#     print("Only when a is equal to 10 since we checked other cases", a)
#     # we could do more stuff here when a is not larger than 10
# # # # # #
# print("Back to normal program flow which always runs no matter what a is")
# # # # # #
# # # # # #
# # # # # # #
# # # # without else both of these could run
# a = 20
# # a = 7
# if a > 5:
#     print("A is larger than 5")
# if a > 10:
#     print("a is larger than 10")
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # # # if else elif
# # # # # a = 190
a = int(input("give me an a! "))
if a > 10:
    print("a is larger than 10")
    print("This will only happen when a > 10")
    if a >= 200: # so we can nest ifs inside another if
        print("a is truly big over  or equal 200")
    else:
        print("a is more than 10 but no more than 199")
elif a < 10:
    print("a is less than 10", a)
else: # if a == 10
    print("a is equal to 10", a)
# # #
# # # # print("This will always happen no matter the a value")
# # # #
# # # # b = -8500
# # # # b = 6
# # # # b = 555
# # # # b = 9000
# # # # if b < 0:
# # # #     print("Less than 0", b)
# # # # elif b < 10:
# # # #     print("Less than 10 but more or equal to 0", b)
# # # # elif b < 9000:
# # # #     pass # empty operation
# # # # #     print("At least 10 but less than 9000", b)
# # # # else:
# # # #     print("9000 or more!", b)
# # # # #
# # # # if b < 0:
# # # #     print("Less than 0", b)
# # # #
# # # # if b < 10:
# # # #     print("Less than 10", b)
# # # #
# # # # if b < 9000:
# # # #     print("less than 9000", b)
# # # # else:
# # # #     print("9000 or more!", b)
# # # # # #
# # # # c = None
# # # # c = 5
# # # # if c == None:
# # # #     print("There is Nothing")
# # # # else:
# # # #     print("There is something")
# # # # # #
# # # #
if 2 < 3 < 8 < a:
    print(f"2 < 3 < 8 < {a}is it a True statement? ", 2 < 3 < 8 < a)
else:
    print(f"2 < 3 < 8 < {a} is it a True statement?", 2 < 3 < 8 < a)