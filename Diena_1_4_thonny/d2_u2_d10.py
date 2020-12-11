     
height = input("What is the height of the room in m?")
height = float(height)
width = input("What is the width of the room in m?")
width = float(width)
length = input("What is the width of the room in m?")
length = float(length)
room_volume = round(height * width * length, 2)
print(f"The volume of the room is {room_volume} m^3.")