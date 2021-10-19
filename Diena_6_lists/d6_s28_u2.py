cubes = []
number_one = int(input("Please enter number: "))
number_two = int(input("Please enter another number: "))
for n in range(number_one, number_two+1):  # so range will take less memory than list for looping
    cube = n**3  
    print(f"{n} cubed:{cube}")
    cubes.append(cube)
print(f"All Cubes 'i³' = {cubes}")