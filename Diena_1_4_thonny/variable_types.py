myName = "Valdis"
print(f"My name is {myName}") # f-strings new in Python 3.6 and above
print("My name is " + myName) # older style
print("My name is ",len(myName),"characters long")
print(type(myName))
# # comments are for humans not for computers
myName = 7 # in Python you can change data type dynamically
myName = "Valdis"
print(f"My name is {myName}")
print(type(myName))
mySpeed = 150 # so new variables are made automatically
print(type(mySpeed))
# myspeed = 95
print(f"{myName} is driving {mySpeed} km/h fast")
print(myName + " is driving " + str(mySpeed) + " km/h fast")
# mySpeed = str(mySpeed) # type casting from whatever to str
# print(myName + mySpeed)
myFloat = 3.1415926
print(myFloat, type(myFloat))

print(0.1+0.2-0.3) # reason for this is that some numbers are impossible to represent under floats
result = 0.1+0.2
print(result)
clean_result = round(result, 2) # 2 digits after comma
print(clean_result)
print(clean_result-0.3)

# Boolean types
isRaining = False
isCold = True
isSnowing = True
print(isRaining, type(isRaining))
print(isCold, type(isCold))

my_empty = None # so nil, null type
print(my_empty, type(my_empty))

print(isRaining + isCold + isSnowing)
print(isCold + 20)

import datetime
start = datetime.datetime.now()
print(start)
print(type(start))
print("Printing is pretty slow actually")
end = datetime.datetime.now()
delta = end - start
print(f"It took {delta} s to print a few lines")

# # a stands for amazing
# # common short variables
# # t - temp or text
# # c for character , Python does not have character so string of length one
# # x,y for coordinates
# # i,j for iterators for looping
# a = 10
# b = 20
# tmp = a
# a = b
# b = tmp
# print(a,b,tmp)
# # in Python we do not need tmp, we can swap values in one step
# a, b = b, a
# print(a,b)
# # typically Boolean values have is in front of them
# isSkyBlue = True
# isNightOrange = False
# print(isSkyBlue, type(isSkyBlue))
# print(True, type(True))
# print(False, type(False))
# my_variable_1 = 14342
# my_variable_2 = "Hmm maybe we need better names for variables"
# my_empty_variable = None
# 
# # composite data types part of Python, more on those separately
# myList = [1,2,3,5,6,7,10000,-535,"even myname"]
# print(myList,type(myList))
# myDictionary = {'key':'value', 'atslēga':'vērtībā'}
# print(myDictionary.items(),type(myDictionary))
# myTuple = (1,2,None,"Badac",3.2) # for storing fixed values
# print(myTuple,type(myTuple))
# mySet = {1,1,5,3,6,2,6,7}
# print(mySet, type(mySet))
