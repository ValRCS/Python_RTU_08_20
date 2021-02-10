my_name = "Valdis" # string data type
# # in Python we need to specifiers for variables
# # DRY - Do not repeat yourself
print(my_name)
print(f"Why hello there {my_name}!") # formatted string from Python 3.6+
print("How are you", my_name, "?")
print(type(my_name))
print("my_name", my_name)
my_other_name = 'Voldemārs'
print(my_name, my_other_name)
# my_name so called snake case
# myName # camelCase in Python is not used as much
# vārds = "Valdis" # please do NOT use non English variable names
a = 5 # int - integer
print(type(a))
a = "Justsome text"
print(type(a)) # so types can change dynamically but prefer to not change often
a = 6
b = 7.5 # float so Duck Typing types are adjusted dynamically 
print(a,b)
c = a + b # so expression will be evaluated first on the right
d = -100 # also an integer
print(a,b,c,d)
# # print(type(my_name))
# # print(type(a),type(d))
# # print(type(b),type(c))
print(my_name + " " + my_name)
print(f"{my_name} {my_name}") # so same result as above
drink = "alus "
stiff_drink = drink*5
print(drink*5)
print(stiff_drink)
# # # 
print(f"My name is {my_name}") # f-strings new in Python 3.6 and above
print("My name is " + my_name) # older style with string concatenate
print("My name is ",len(my_name),"characters long")
# print(type(my_name))
# # # # # comments are for humans not for computers
# my_name = 7 # in Python you can change data type dynamically
# print("hmm my_name is now", type(my_name), my_name)
# # for clarity let's not do it too often
# my_name = "Valdis"
# print(f"My name is {my_name}")
# # print(type(my_name))
my_speed = 150 # so new variables are made automatically
print(type(my_speed))
my_specd = 180 # so types in variable names will not be picked up
my_speed = 95
print(f"{my_name} is driving {my_speed} km/h fast")
speed_report = f"{my_name} is driving {my_speed} km/h fast"
print("speed_report") # this is just text
print(speed_report) # this whatever is in variable speed_report
# # # f strings will cast ints,floats to str automatically
# # i will need to cast my_speed to str
# print(my_name + " is driving " + my_speed + " km/h fast")
print(my_name + " is driving " + str(my_speed) + " km/h fast")
my_str_speed = str(my_speed)
my_str_speed_int = int(my_str_speed) # i can go back
# # # # my_speed = str(my_speed) # type casting from whatever to str
# # # print(my_name + my_speed)
my_float = 3.1415926
print(my_float, type(my_float))
# # #
my_div = 10/3
print(my_div)
my_round_float = round(my_div, 4) # digits after comma
print(my_round_float)
print(round(3.9))
my_int = int(my_div) # so similar to floor which is also available
print(my_int)
print(0.1+0.2-0.3) # reason for this is that some numbers are impossible to represent under floats
result = 0.1+0.2 
print(result)
clean_result = round(result, 2) # 2 digits after comma
print(clean_result)
print(result-0.3)
print(clean_result-0.3)
print(f"CLEAN: {clean_result:.5f}") # if i want 5 digits after comma
print(f"UNCLEAN: {result:.8f}") # if i want 8 digits after comma
my_pi = round(my_float, 2)
print(my_pi)
print(a**2) # ** for power
print(a**3) # a cubed
print(a**b) # a to the b-th power
print(36**0.5) # so square root
# 
print(10%7) # reminder atlikums (mod)
print(20%7) # also reminder
print(13%2)
print(14%2)
print(10/7) # normal division
print(10//7) # just whole division, meanting just the int part
print(a)
# print(20//6)
print((a+b)*(c-d))
calc_result = (a+b)*(c-d)
print(calc_result)
# # # 
# # # Boolean types
is_raining = False
isCold = True
isSnowing = True
print(is_raining, type(is_raining))
# # print(isCold, type(isCold))
# # # 
my_empty = None # so nil, null type
print(my_empty, type(my_empty))
# # # 
# # # print(is_raining + isCold + isSnowing)
# # # print(isCold + 20)
# # # 
# # # import datetime
# # # start = datetime.datetime.now()
# # # print(start)
# # # print(type(start))
# # # print("Printing is pretty slow actually")
# # # end = datetime.datetime.now()
# # # delta = end - start
# # # print(f"It took {delta} s to print a few lines")
# # # 
# # # # # a stands for amazing
# # # # # common short variables
# # # # # t - temp or text
# # # # # c for character , Python does not have character so string of length one
# # # # # x,y for coordinates
# # # # # i,j for iterators for looping
# # # # a = 10
# # # # b = 20
# # # # tmp = a
# # # # a = b
# # # # b = tmp
# # # # print(a,b,tmp)
# # # # # in Python we do not need tmp, we can swap values in one step
# # # # a, b = b, a
# # # # print(a,b)
# # # # # typically Boolean values have is in front of them
# # # # isSkyBlue = True
# # # # isNightOrange = False
# # # # print(isSkyBlue, type(isSkyBlue))
# # # # print(True, type(True))
# # # # print(False, type(False))
# # # # my_variable_1 = 14342
# # # # my_variable_2 = "Hmm maybe we need better names for variables"
# # # # my_empty_variable = None
# # # # 
# # # # # composite data types part of Python, more on those separately
# # # # myList = [1,2,3,5,6,7,10000,-535,"even my_name"]
# # # # print(myList,type(myList))
# # # # myDictionary = {'key':'value', 'atslēga':'vērtībā'}
# # # # print(myDictionary.items(),type(myDictionary))
# # # # myTuple = (1,2,None,"Badac",3.2) # for storing fixed values
# # # # print(myTuple,type(myTuple))
# # # # mySet = {1,1,5,3,6,2,6,7}
# # # # print(mySet, type(mySet))
# # # 