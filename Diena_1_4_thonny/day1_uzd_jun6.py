name="Imants"
print(5*name)
print(name * 7)
print(365*24*60*60)
print(10**100)
a="ba"
b="na"
print(f"{a}"+b*4)
print(f"{a}{b*4}")
also_string = 'vakars'
# single quotes are just like double quotes in Python

# what do we do if we need { inside f-strings
print("My name is {name}")
print(f"My name is {name}")
print(f" I can use curly braces inside f-strings with {{ is that right {name} ?")
multi_line = "Text\nO0ver multiple\nlines"
print(multi_line)

print("🥛")
milk = "🥛"
print(milk, ord(milk))
print(ord("ā"), ord("Ā"), ord('€'))

# all CAPS signify constants
# but Python does not enforce it
PI = 3.1415926
# PI is a variable just like others
print(PI)
Alabama_PI = round(PI)
print(PI, Alabama_PI)
# I can specify digits of PI to round
print(PI, round(PI,2), round(PI,4), round(PI,6))
# so pi to 4 digits
PI_4 = round(PI,4)
print(PI_4)
var1=";"
print(ord(var1))
var2=";"
print(ord(var2))
# I L 1 used to be very similar
# now most monospace fonts will differentiate
print(var1 == var2)