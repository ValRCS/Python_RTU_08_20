#The second
length = input("What is length of the room? ")
width = input("What is the width of the room? ")
height = input("What is the height of the room? ")
 
length = float(length)
width = float(width)
height = float(height)
 
volume = length*width*height
volume = round(volume, 2)
 
print(f"The volume of room is {volume} cubic meters!")