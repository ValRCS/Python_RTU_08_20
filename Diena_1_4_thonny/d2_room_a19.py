# 2. Uzdevums
# Uzdod 3 jautājums par telpas platumu, garumu, augstumu
wide = input("how wide is the room?")
long = input("how long is the room?")
high = input("how high is the room?")
 
# Uzrāda cik liels būs telpas tilpums
volume = float(wide) * float(long) * float(high)
volume = round(volume, 2)
print(f"Room volume is {volume} m3")