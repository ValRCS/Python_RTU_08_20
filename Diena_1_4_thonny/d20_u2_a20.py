## 2. Task
## Ask width, length, height to calculate volume
width = float(input("What is the width of room?"))
length = float(input("What is the length of room?"))
height = float(input("What is the height of room?"))
volume = round(width * length * height, 4)
print(f"Volume of the room is {volume}")