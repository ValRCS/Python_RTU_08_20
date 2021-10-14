my_number_cubes = []
start = int(input("enter start "))
end = int(input("enter end "))
my_number_range = list(range(start, end+1)) # a bit faster would be to use range in next line
for n in my_number_range:
    cube = n**3  # will save time if this operation is heavy
    print(f"{n} kubā:{cube}")
    my_number_cubes.append(cube)
print(my_number_cubes)