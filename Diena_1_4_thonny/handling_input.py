# my_name = input("What is your name friend? ")
# print(f"Wow that is a nice name {my_name}") # i am using f-string formatting which is available in Python since 3.6 and up
# # this lets me put variable directly into my string text
# # otherwise I would have to do
# print("Wow that is a nice name " + my_name) # same as above but gets tricky for longer strings
#
# a = input("what number you want to double? ")
# double_str_a = a * 2
# print(f"Cool {a} doubled is {double_str_a}, or is it ?")
# #solution is to cast to the type we want
# my_float = float(a) # is should do this before int cast because casting to int would lose the values
# float_square = my_float**2
# print(f"Cool {my_float} squared is {float_square}, or is it ?")
# a = int(my_float) # so a became an integer # we could also use float(a) if we want floats
# double_a = a * 2
# print(f"Cool {a} doubled is {double_a}, or is it ?")

a = 3.1415926
round_a = round(a,4) # 4 digits after comma
print(a, round_a, round(a,2), round(a))

my_result = 0.1+0.2
print(my_result)
my_zero = my_result-0.3
print(my_zero) # that is like almost zero 17 zeros after comma....
my_zero = round(my_zero)
print(my_zero)