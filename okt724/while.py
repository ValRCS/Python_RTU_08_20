# cikli dod mums iespēju darīt līdzigas darbības atkartoti
# print("Hello")
# print("Hello")
# print("Hello")
# how about 100 times, 1 million times?

# pamat konstrukcija while ciklam
# daram kaut ko kamēr mums ir patiess nosacījums

# while True:
#     print("Hello Monday!")
    
# print("Hello Tuesday")
print("Starting our looping program")

i = 0
while i < 5:
    print(f"Hello there Nr. {i}")
    # we need to change value of i so eventually we can leave our loop
    i += 1 # same as i = i + 1 we add 1 to i # Python has no i++
    print(f"still inside loop i is now {i}")
    # here I go back to start of while and check i < 5 again

print(f"Outside loop and i is {i}")

# we can also go down
floor = 9 # i could have reused i since i is a common iterator name 
while floor >= 0:
    print(f"I am on floor {floor}")
    # we can add if inside our loop
    if floor % 2 == 0:
        print("I am on even floor", floor)
    else:
        print("I am on odd floor", floor)
    floor -= 1 # same as floor = floor - 1
    
# i have reached floor hopefully 0
print(f"Whew I should be on underground parking floor {floor}")
    
# often I need to save some results
# i could use some variable for that
total = 0 # do not use sum as variable name, it is semi-reserved in Python
i = 100
while i <= 110:
    print(f"adding {i} to {total}")
    total += i # so same as total = total + i
    # i still need to change i else i will get stuck
    i += 2 # so step 2
# outsid loop
print(f"At end total is {total} and i is {i}")
    

