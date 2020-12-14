print(2*2 == 4) # so == compares values returns Boolean
print(2*2 == 5)
a = 2
b = 3
c = 3
result = 4
d = 5
unused_var = 6
print(a*a == result)
print(a+b == result)

# we can also do greater and smaller comparison
print("a < b", a < b)
print("b < a", b < a)
print("a < b < result", a < b < result) # so i can compare them in chain
print("a < b < result < 9000", a < b < result < 9000) # so i can compare them in chain

print("a <= b", a <= b)
print("b <= a", b <= a)
print("b <= 3", b <= 3)

print("a >= b", a >= b)
print("b >= a", b >= a)
print("b >= 3", b >= 3)

print("2 != 3", 2 != 3) # checking for inequality returns true when values are not equal
print("2 != 2", 2 != 2) # False statement because 2 is in fact equal to 2

print("0 == False", 0 == False) # again so 0 and False are both falsy values
print("1 == True", 1 == True)
print("0 == '' ", 0 == "")

# less used is checking for actual objects in memory with is
print("are b and c pointing to same memory address", b is c)
name = "Valdis"
also_name = "Valdis"

print("name == also_name", name == also_name)
print("name points to same place as also_name", name is also_name)

# we can save our comparision results
b_gt_a = b > a # evaluation is from the right to the left
# print(a == not_defined_var) # this will be an NameError

