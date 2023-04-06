# we can use Booleans to make choices about paths
# our program takes
a = 2 # pretend this is input
# if lets us choose whether to run some code
# notice colon: and indentation
if a < 10:
    # we entered if block only when a < 10 is True
    print(f"{a} is less than 10 ? {a < 10}")
    print("We are still in block where a < 10")
# important this 2nd if is not related to first
if a > 10:
    print("a is more than 10", a)
# we are back main code 
print("This will always print")

# we might want to choose just one path out of two
a = 20
if a < 20:
    print(f"a < 20 ? {a < 20}")
else: # this meanswhen a is not less than 20
    print("a is not less than 20")
    print("a is ", a)
    
# if we need to make more than two paths but just one should be chosen
# for example one of 3 roads in the fairy tale
a = 2
number = int(input("Enter an integer"))
if number > 42:# first check
    print("Your guess is too much", number)
elif number < 42: #2nd check
    print("You guessed too litle", number)
# elif a*2 == 4:
#     print("Not related to number")
#     print("a * 2 is 4", a)
else:
    print("Wow nice number, 42 is answer to everything", a)
