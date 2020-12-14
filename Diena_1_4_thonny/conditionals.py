# a = 8
# if a > 10: # in Python when you see : next line will be indented
#     # runs only when statement after if is True
#     print("Do this when a is larger than 10")
# 
# 
# print("This will always print")
# 
# 
# if a > 10: # in Python when you see : next line will be indented
#     # runs only when statement after if is True
#     print("Again Do this when a is larger than 10")   
# else:
#     print("Only when a is less or equal to 10")
#     # we could do more stuff here when a is not larger than 10
#     
# print("Back to normal program flow")
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# # if else elif
# a = 190
a = int(input("give an a! "))
if a > 10:
    print("a is larger than 10")
    print("This will only happen when a > 10")
    if a >= 200:
        print("a is truly big over  or equal 200")
    else:
        print("a is more than 10 but no more than 199")
elif a < 10: 
    print("a is less than 10")
else: # if a == 10
    print("a is equal to 10")
    
print("This will always happen no matter the a value")
