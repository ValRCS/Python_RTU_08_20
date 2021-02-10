#task 2
length = float(input("What is the length of the room ? "))
width = float(input("What is the width of the room ? "))
height = float(input("What is the height of the room ? "))
total = round(length*width*height, 2)
print(f"Room is {total} cubic meters in volume")