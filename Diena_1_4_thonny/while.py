# print("Hello")
# print("Hello")
i = 0
while i < 5:
    print("Hello No.", i)
    i += 1
print("Always happens once loop is finished")
print("i is now", i)
i = 10
while i > 0:
    print("Going down the floor:", i)
    # i could do more stuff
    i -= 2
print("Whew we are done with this i:", i)

i = 20
while True:
    print("i is",i)
    if i > 28:
        break
    i += 2
    
while True:
    res = input("Enter number or q to quit ")
    if res == "q":
        print("No more calculations today")
        break
    elif res == "a": # TODO check if if the input is text
        print("I can't cube a letter a")
        continue # means we are not going to try to convert "a" to float
    num = float(res)
    print(f"My calculator says cube of {num} is {num**3}")

print("All done whew!")


    
