my_float = 3.1415926
my_int = int(my_float) # makes an integer out of float
my_rounded_int = round(my_float) # also integer but rounds
my_rounded_int_2_digits = round(my_float, 2) # 4 digitas after comma
my_rounded_int_4_digits = round(my_float, 4) # 4 digitas after comma

a = 3.5
b = int(a) # we get 3
c = round(a) # we will get 4

float_again = float(b) # this will create 3.0 float

# there is also floor and ceil function
import math
d = math.floor(a)
e = math.ceil(a)

my_number_string = "3.14" # this is a string
my_number = 3.14
float_from_string = float(my_number_string) # this will only work on strings which have floating numbers or
my_integer_string = "9001" # just text for now
number_from_integer = int(my_integer_string)

back_to_string = str(my_number)


