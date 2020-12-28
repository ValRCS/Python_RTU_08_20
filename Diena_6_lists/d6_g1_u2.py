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

start_num = int(input("Please insert begining number: "))
end_num = int(input("Plese insert end number: "))
cubes = [f'{num} kubā: {num**3}' for num in range(start_num, end_num+1)]
print(cubes)