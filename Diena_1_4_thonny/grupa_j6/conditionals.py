# conditionals is how we make code execute on certain conditions only
is_late = True
# is_late = False

if is_late: # so in Python after : we have indentation
    # in Python we do not need {
    print("It is running late..")
    print("is it late?", is_late)
    # we are still inside if block
    # we could do more stuff if it is late
    # so other languages would have } or endif here
# now we are outside
print("This is main block, will always run")

# we could do everything with just if
# but often we want to choose just one option out of two
# so two roads - pick one
# so we have optional else
is_summer = True
is_summer = False

# we will pick a single road
if is_summer:
    print("Whew it is summer")
    print("Going to enjoy the sun 🌞")
    # could do more here when is_summer is True
else: # nothing else is possible just that is_summer is False
    print("Oh, not summer, getting cold....")
    print("Going to start my fire 🔥")
    # of course we could do more cold weather stuff here
# back to normal block - main block
print("Back to normal things")

# how about 3 exclusive paths - meaning only one is possible
# we use elif (else if in other languages)

# number = 50
# number = 20
number = 42

if number > 42:
    print(f"Oh this {number} is over 42")
    print("Pick something smaller")
elif number < 42: # so another comparison
    print(f"Oh this {number} is less than 42")
    print("Pick something bigger")
# we could do more elif here for more choices
else: # so only 42 remains that is number == 42
    print("Cool you picked the answer to the universe and everything!")
    print(number)

# again back to main block
print("We are back in main block")

# we can do nested ifs meaning if inside if
number = 500

if number > 100:
    print("pretty big number over 100", number)
    if number > 1_000_000: # for big numbers we can use _ for readability
        print("big number over million", number)
    else:
        print("so number between 101 and 1 000 000 ==>", number)
else:
    if number < 0:
        print("negative number", number)
    else:
        print("number between 0 and 100", number)
        
# so we have 4 paths

# we could do even more nesting as many levels as we want

# however in practice we do not want to go over 3 or 4 levels of nesting
# it makes code very hard to debug and follow

# since Python 3.8 we have match case for multiple choice

        
