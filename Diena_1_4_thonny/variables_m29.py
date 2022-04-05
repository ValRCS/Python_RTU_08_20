# variables in Python are created as soon as we start using them
# so I need to assign something to a variable
# then I can use this variable
# print(name)  # will throw an error, name is not yet defined
name = "Valdis"  # variable name will point to a string "Valdis"
print(name)  # this is a variable with string contents
print("name") # this is a just string
print(f"Why hello there {name}! ")  # f-strings syntax
print(f"How about some math {name}?")
a = 2
b = 3
c = a*b
text_result = f"{a}+{b}={c}"
print(text_result)
print(type(text_result), type(c))
c = "Some text" # we can change types on the fly
# dynamic typing
# generally better practice to stick with same type
print(c, type(c))

c = 50 # this would be better , we can overwrite but stick with same type
print(c, type(c))

big_number = 9_000_000 # _ we can use for cosmetic reasons
print(big_number)
really_big_number = 18_000_000_342_423_524_532_567
print(really_big_number)