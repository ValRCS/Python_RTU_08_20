# 2. uzdevums
width = float(input('kāds ir telpas platums? (m)'))
length = float(input('kāds ir telpas garums? (m)'))
height = float(input('kāds ir telpas augstums? (m)'))
volume = width * length * height
volume = round(volume, 2)
print(f'telpas tilpums ir {volume} m³')
print(f'telpas tilpums ir {volume} m\U000000B3')
print(ord("³"))
print(ord("Ā"))