myName = "Valdis"
print(f"My name is {myName}")
# comments are for humans not for computers
# myName = 6
# print(f"My name is {myName}")
mySpeed = 150
mySpeed = 95
print(f"{myName} is driving {mySpeed} km/h fast")
mySpeed = str(mySpeed) # type casting from whatever to str
print(myName + mySpeed)
myFloat = 3.14159
print(myFloat, type(myFloat))
# a stands for amazing
# common short variables
# t - temp or text
# c for character , Python does not have character so string of length one
# x,y for coordinates
# i,j for iterators for looping
a = 10
b = 20
tmp = a
a = b
b = tmp
print(a,b,tmp)
# in Python we do not need tmp, we can swap values in one step
a, b = b, a
print(a,b)
# typically Boolean values have is in front of them
isSkyBlue = True
isNightOrange = False
print(isSkyBlue, type(isSkyBlue))
print(True, type(True))
print(False, type(False))
my_variable_1 = 14342
my_variable_2 = "Hmm maybe we need better names for variables"
my_empty_variable = None

# composite data types part of Python, more on those separately
myList = [1,2,3,5,6,7,10000,-535,"even myname"]
print(myList,type(myList))
myDictionary = {'key':'value', 'atslēga':'vērtībā'}
print(myDictionary.items(),type(myDictionary))
myTuple = (1,2,None,"Badac",3.2) # for storing fixed values
print(myTuple,type(myTuple))
mySet = {1,1,5,3,6,2,6,7}
print(mySet, type(mySet))
