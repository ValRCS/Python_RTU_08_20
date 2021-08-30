# print("Hello")
# print("Hello")
# print("Hello")
i = 1
while i < 5: # while loops are for indeterminate time
    print("Hello No.", i)
    print(f"Hello Number {i}")
    i += 1  # i = i + 1 # we will have a infinite loop without i += 1
print("Always happens once loop is finished")
print("i is now", i)
i = 10
while i > 0:
    print("Going down the floor:", i)
    # i could do more stuff
    i -= 1 # i = i - 1
print("Whew we are done with this i:", i)

total = 0 # do not use sum as name for variable
i = 20
while i <= 30:
    total += i
    print(f"After adding {i} total is {total}")
    i += 2
print(f"i is {i} total is {total}")

start = 20
end = 40
step = 4
i = start
while i <= end:
    print(f"i is {i}")
    i += step
# 
i = 20
while True:
    print("i is",i)
    if i > 28:
        break # with break with break out of loop
    i += 2
    
print(i)

i = 20
active = True
is_raining = True
while active and is_raining:
    print(f"Doing stuff with {i}")
    i += 3
    # TODO update weather conditions
    if i > 30:
        active = False
#     
while True:
    res = input("Enter number or q to quit ")
    if res.lower().startswith("q"):
        print("No more calculations today")
        break
    elif res == "a": # TODO check if if the input is text
        print("I can't cube a letter a")
        continue # means we are not going to try to convert "a" to float
    num = float(res)
    print(f"My calculator says cube of {num} is {num**3}")
# 
print("All done whew!")

outer_flag = True
inner_flag = True
i = 10
while outer_flag:
    print(i)
    while inner_flag:
        res = input("Enter q to quit")
        if res == 'q':
            print("got q lets break from inside")
            break
    i += 1
    if i > 14:
        print("outer break about to happen")
        break
# 
# 
#     
# 