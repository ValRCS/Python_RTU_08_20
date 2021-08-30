PI = 3.1415926 # longer values of PI are available from libraries
print(PI)
e = 2.71 # could use this perhaps
print(e)
# for floats we use . 
my_not_float = 2,56223 # this will not work properly
# it will create a tuple

this_is_float = 2.46345
# type casting - changing one data type to another
my_int = int(this_is_float)
print(my_int, this_is_float)

float_again = float(my_int)
print(my_int, float_again)

print(0.1+0.2)
result = 0.1+0.2-0.3 # this will not be quite zero
print(result)
rounded_result = round(result)
print(rounded_result)
print(PI, round(PI,4))


