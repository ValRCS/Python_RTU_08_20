print("Day 2")
my_day = "Day 2"
print(my_day)
print(f"Make {my_day}")
# Python has dynamic data types
# we can change them
my_day = 2
print(f"My day is now {my_day}")
print(my_day * 10)
my_day = str(my_day) # we can go back to string
print(f"My day is now {my_day}") # looks same right?
print(my_day * 10) # different data types produce different results
my_big_string = my_day * 10
my_big_day = int(my_big_string) # I can conver strings to integers if they make sense
print(my_big_day, my_big_day + 5000)
# almost everything can be converted to string
# not everything will be convertable to int or float
name = "Valdis"
# i cant convert my name to integer
# my_number = int(name) # will throw ValueError
# for single characters we can get Unicode code
print(ord("V"), ord("a"), ord("ā"), ord('€'), ord("😁"))
print(chr(86), chr(97), chr(257), chr(8364), chr(128513))
