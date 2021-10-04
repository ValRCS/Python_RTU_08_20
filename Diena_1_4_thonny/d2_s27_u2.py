#2.uzdevums
lenght=float(input(f"How long m are your room?"))
# print(f"Lenght is {lenght} m")
width=float(input(f"Lenght is {lenght} m\nHow wide m are your room?"))
print(f"Width is {width} m")
height=float(input(f"How high in m are your room?"))
print(f"Height is {height} m")
 
volume=lenght*width*height
volume=round(volume, 3) # so 3 digits after .
print(f'Your room volume is {volume} m³ 😄') # so unicode supescript three