# conditionals let us run only code on certain conditions

is_late = True
# is_late = False

if is_late:
    # we have a conditional block
    print("is late?", is_late)
    print("We run this")
    # i can run more lines here
    print("I also run this")
# conditional block has ended
print("This always runs")

is_summer = True

# we can choose one of TWO roads, just one
if is_summer:
    print("it is summer")
else: # else here is attached to if
    print("hmm it is not summer...")



# how about 3 exclusive paths? only one would proceed
number = 42

if number > 42:
    print(f"Oh {number} is over 42")
    print("Aim a litle lower")
elif number < 42:
    print(f"Oh {number} is over 42")
    print("Aim a litle lower")
else: # so only 42 remains... as Sherlock Holmes would know - or Douglas Adams
    print(f"Oh you found the answer to everything!")
    print(number)

# we are out  
print("We are out of our if elif else block")