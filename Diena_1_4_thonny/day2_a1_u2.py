# 2 uzd
precision = 2
length = float(input("How long is the room? (meters)"))
height = float(input("How high is the room? (meters)"))
width = float(input("How wide is the room? (meters)"))
volume = length * height * width
volume = round(volume, precision)
print(f"Room volume is {volume} in m³")  
print(f"Room volume is {volume} in m\u00B3")  # for unicode under 65535
print(f"Room volume is {volume} in m\U000000B3")  # for any unicode code

print(ord("³")) # get Unicode number for symbol in decimal
print(chr(179))  # prints symbol by its Unicode value in decimal
print(ord("ā")) # get Unicode number for symbol in decimal
print(chr(257))  # prints symbol by its Unicode value in decimal