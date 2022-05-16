# print("Valdis"*5)
# print(print) # will print a reference to print function
# print(365*24*60*60) #how many seconds are in this year
# print(10**100) #ten raised to the power of a hundred
# print("Ba"+"na"*4) #using only Ba and na get Banananana
# print(("Ba"+"na")*4)
# print(("Ba"+"na ")*4)
seconds_in_a_year = 365*24*60*60  # assignment operator
print(seconds_in_a_year)
name = "Valdis"
print(name) # this is printing contents of variable
print("name") # this is string literal
print("My name is " + name) # there is also f-strings

print("Cool I can print 😁 as well") # full Unicode support
print("Latvijas kaķus arī var drukāt 🐱")

#f-strings since Python 3.6 - the coolest thing since sliced bread
print(f"My name is {name}")
print(f"There are {seconds_in_a_year} seconds in a year")
print("There are {seconds_in_a_year} seconds in a year")
print("2+2={2+2}")
print(f"2+2={2+2}") # so i can evaluate 2+2 inside {2+2}
# so i can use variable multiple times in my string
print(f"Oh {name} my name is also {name}, funny isn't it?")
print(f"There are {365*24*60**2} (sec.)")
print('If I need double quotes " like this inside" then use single quotes')

