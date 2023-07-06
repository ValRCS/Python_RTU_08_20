# conditional execution - branching
# idea do something only on some condition
# if True: # in Python after : there is usually indentation
#     # if block starts here
#     print("Inside True block")
#     print("Still inside")
#     # can do more stuff
# # outside if block
print("Outside in general block")
# usually we will have some variable
a = 2
b = 4
if a < b:
    # inside if
    print("a < b is true indeed", a < b)
    print(a, b)
    # could keep doing whatever needs to be done when a < b
# back outside
print("Outside if")

# we could also create exclusive two paths with if else
# a = 2023
if a > b:
    print("a is larger than b", a,b)
    # more stuff to do when a > b
else: # so a <= b
    print("so a <= b", a, b)
    
# if we need more than 2 exclusive paths (only one path taken)
# we generally use else elif (elif elif...) else construction

guess = 1000
guess = -33
guess = 42
answer = 42
if guess > answer:
    print("You guessed too high")
    print(guess, answer)
elif guess < answer:
    print("You guessed too low")
    print(guess, answer)
else: # so only one possibility remains guess == answer
    print("You guessed it !", guess, answer)
    # and more congrats here
    
# we can do nested ifs
# in practice the flatter the code the easier it is to read
if answer > 30:
    print("answer is over 30", answer)
    if guess < 50:
        print("Guess under 50", guess)
    else:
        print("guess 50 or more", guess)
else:
    print("answer is 30 or more", answer)
    if a >= 2:
        print("a is >= 2", a)
    else:
        print("a < 2", a)
        
# from Python 3.10 we have match case - similar to switch case
# but more powerful
# this match case can replace loooong if elif elif ... elif else chains

letter = "b"
letter = "Valdis"
# "stringie" and 'stringie' are exactly the same in Python
match letter:
    case 'a':
        print("oh and a!", letter)
        # notice no break needed
    case 'b':
        print("aha b it is", letter)
    case 'Valdis':
        print("you found Valdis!", letter)
    case _: # we use _ for default catch all
        print("uknown string", letter)
        
# also match case can math on types and also on
# complex collections with specific number of items
# https://peps.python.org/pep-0636/

