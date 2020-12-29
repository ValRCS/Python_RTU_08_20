# uzdevums 2
start = int(input("Enter first number: "))
end = int(input("Enter second number: "))
my_list = [i**3 for i in range(start,end+1)]
print(my_list)



#2.uzdevums
 
# start = int(input("Please, enter first number: "))
# end = int(input("Please, enter last number: "))
# i = start
# cube_list = []
# while i <= end:
#     a = i ** 3
#     cube_list.append(a)
#     print(f"{i} cube is: {a}")
#     i += 1
# print(f"All cubes: {cube_list}")