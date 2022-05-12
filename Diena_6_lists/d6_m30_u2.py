#2.uzdevums

### Task No.2
my_numbers = []
cube_list = []
while True:
    user_input_bottom = input("Enter the bottom range value: ")
    user_input_top = input("Enter the top range value: ")
    try:
        # check = float(user_input_bottom)
        # check = float(user_input_top)
        bottom = int(user_input_bottom)
        top = int(user_input_top)
        my_numbers = list(range(bottom, top+1))
        for i in my_numbers:
            cube = i**3
            print(f"{i} kubā: {cube}")
            cube_list.append(cube)
        print("My list: ", my_numbers)
        print("Cube list ", cube_list)
        break
    except ValueError:
        print("Sorry not a number! Please try again: ")
        continue # back to front of while , ignoring rest of loop below