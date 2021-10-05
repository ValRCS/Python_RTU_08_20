#2.uzdevums
width = float(input("What is the width of this room in m?"))
print(width)
lenght = float(input("What is the lenght of this room in m?"))
print(lenght)
height = float(input("What is the height of this room in m?"))
print(height)
total = round(width*lenght*height, 2)
print(f"Total volume/capacity of the room is {total} m³")