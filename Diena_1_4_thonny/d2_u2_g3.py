#uzdevums 2
print("Programma aprēķina telpas tilpumu")
width = float(input("Ievadi telpas platumu(mm): "))
length = float(input("Ievadi telpas garumu(mm): "))
height = float(input("Ievadi telpas augstumu(mm): "))
# TODO parsing of . and , both as float separators
volume_result = round(width*length*height/1_000_000_000, 2)
print(f"Telpas tilpums ir {volume_result} km\u00B3 so also km³")
# print(f"Telpas tilpums ir {round(width*length*height,2)} kubikmetri")