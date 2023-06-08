# Ask for the dimensions of the room
length = float(input("What is the length of the room in meters? "))
width = float(input("What is the width of the room in meters? "))
height = float(input("What is the height of the room in meters? "))
 
# Calculate the volume of the room
volume = length * width * height
 
# Display the result
print(f"The volume of the room is {volume:.2f} cubic meters (m³).")
volume = round(volume, 2)
print(f"The volume of the room is {volume} cubic meters (m³).")