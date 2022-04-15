# True, False
print(type(True))
# print(type(true))
is_sky_blue = True
is_sunny = False
print(2*2 == 4) # notice the difference == is comparison
# # do more stuff here
# # do more and more
print("All done")
is_calc_good = 3*3 == 9 # we evaluate from the right side to the left
is_calc_still_good = 2*2 == 5
a = 4 
b = 5
c = 2
print(a == 2*2)
is_calc_still_good = a == 2*2
print("This calculation is", a == c*c )
# # remember python is dynamically typed, types can change
# c = a == 2*2 # c is a bad name for boolean type
# # booleans we generally start with is_something
print(a != b, a != 2*2, c*c != a)
print("Comparing 4s", 4 != 4, 4 == 4)
print(4 > 4, a > 4, a > 3, a > c)
a = 500
print(4 > 4, a > 4, a > 3, a > c)
a = -100
print(a > 4, a > 3, a > c)
print(a < 4, a < 3, a < c)
a = 4
print(a <= 5, a <= 4, a <= 3, a <= c)
print(a >= 5, a >= 4, a >= 3, a >= c)
d = 2
print(c == d) # we check value equality
print(c is d) # we check whether c and d point to the same object
c = 9000
d = 9000
e = 9000
print(c == d) # we check value equality
print(c is d) # we check whether c and d point to the same object
print(c == e, c is e)
myname = "Valdis"
friend_name = "Voldemars"
print(myname > friend_name)
print(myname < friend_name)
friend_name = "Vold"
print(myname < friend_name)
print(len(myname) > len(friend_name), len(myname), len(friend_name))
# 