#Task 3:
x = int(input("Please enter first number: "))
y = int(input("Please enter second number: "))
z = int(input("Please enter third number: "))
# if x <= y <= z:
#     print(x, y, z)
# elif x <= z <= y:
#     print(x, z, y)    
# elif y <= x <= z:
#     print(y, x, z)    
# elif y <= z <= x:
#     print(y, z, x)    
# elif z <= y <= x:
#     print(z, y, x)    
# elif z <= x <= y:
#     print(z, x, y)
# else:
#     print("Quantum malfunction!") # this shouldnt happen

print(sorted([x,y,z]))