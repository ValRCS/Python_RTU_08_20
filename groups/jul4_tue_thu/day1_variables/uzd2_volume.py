#2. Uzdevums
# so consensus is that mm would be better units than m
h = float(input("Augstums?: "))
w = float(input("Platums?: "))
l = float(input("Garums?: "))
# it used to be that l was considered very bad variable name
# why?
# 1 I l used to be very similar on most fonts
# generally short variable names should be used when
# meaning is easy to tell from context and variables fit in one page
# a, b, c usually lack meaning and something more meaningful would be helpful
# n, t, s, i can be good variables depending on context
# of course x,y,z for 3d
# otherwise one or two word variables provide good balance
# very_long_variable_names_not_so_great
volume = h*w*l
print(f"Tilpums: {h*w*l}")
print(f"Volume: {volume:.2f} m³")
# how to show curly braces in f-strings
print(f" {{Sometext}} is {volume:.2f}") # first part is just brackets, Volume is just string
print(" just some text in {brackets}") # no variables