while True:
    try:
        start_number = int(input("Please enter start number:\n"))
        end_number = int(input("Please enter end number:\n"))
        break
    except ValueError:
        print("please enter integer")
        continue

my_list = list(range(start_number, end_number + 1))

cube_list = [n**3 for n in my_list]

another_cube_list = []
for item in my_list:
    cube = item**3
    print(f"{item} in cube: {cube}")
    another_cube_list.append(cube)
print(f"All cubes: {cube_list}")