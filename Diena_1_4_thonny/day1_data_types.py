# exploring different data types
a = 1 # integer
b = 3.1415926 # float
c = "some text" # string
is_snowing = True # boolean data type
is_sunny = False # also boolean
d = None # special None type representing nothing

a = a / 2 # a will be float now!
# a = "some string" # could do it but not good style
print(a,b,c)

# if I did not have object inspector
# i could still find out the type
# using type(my_var) command
print(type(a))
print(type(b))
print(type(c))
print(type(is_snowing))

# i can change one type to another - for many types
# this is called type casting
my_pi = int(b)
print(b, my_pi)
# will I get the full value back?
my_float = float(my_pi)

print(my_float, my_pi)

print("Valdis invented PI:", my_pi)

# what can we do?
#new_text = c + b # can I add str with float??

# I can cast b to str
new_text = c + " " + str(b)
print(new_text)

# there has to be a better way to format strings!!

# from python 3.6 we have f-strings
# formatted strings
name = "Valdis"
university = "RTU"
cabinet = 422

# I did not have to convert cabinet to string
email_footer = f"{name} from {university} at room {cabinet}"

multi_line_text = f"""I can write anything
any lines put {name} inside
put some numbers such as {a}
and so on
"""
print(email_footer)

print(multi_line_text)

# I can use inside {for some operations}
print(f"{a} + {b} == {a+b}")
greeting = f"Hello {name}"
print(greeting)
big_number = 10**100
# i could be doing something else and only need big_number later
print(big_number)



